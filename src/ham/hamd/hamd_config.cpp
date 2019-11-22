// Host Account Management
#include <glib.h>                       // g_main_loop_new(), g_main_context_default(), g_main_loop_run(), g_main_loop_unref(), g_main_loop_quit(), gboolean, etc...
#include <stdlib.h>                     // strtoll(), EXIT_SUCCESS
#include <systemd/sd-journal.h>         // sd_journal_print()
#include <limits.h>                     // LLONG_MIN, LLONG_MAX
#include <errno.h>                      // errno, EINVAL, ERANGE

#include "hamd.h"                       // hamd_config_c
#include "../shared/utils.h"            // true_false()

/**
 * @brief Parse command-line options/arguments
 */
hamd_config_c::hamd_config_c(int argc, char **argv)
{
    GOptionContext  * ctx_p;
    std::string       verbose_help   = "Print extra debug        [" + std::string(true_false(tron_default_m)) + ']';
    std::string       conf_file_help = "Configuration file       [" + std::string(conf_file_default_pm) + ']';

    static const GOptionEntry options[] =
    {
        { "verbose",   'v',  G_OPTION_FLAG_NONE, G_OPTION_ARG_NONE,   &tron_m,       verbose_help.c_str(),   NULL },
        { "conf-file", 'f',  G_OPTION_FLAG_NONE, G_OPTION_ARG_STRING, &conf_file_pm, conf_file_help.c_str(), NULL },
        { NULL,        '\0', G_OPTION_FLAG_NONE, G_OPTION_ARG_NONE,   NULL,          NULL,                   NULL }
    };

    const std::string description =
        "Configuration file parameters:\n"
        "  debug=[yes/no]      Enable additional debug info to the syslog                      [" + std::string(true_false(tron_default_m, "yes", "no")) + "]\n" +
        "  poll_period=[sec]   Daemon's polling period. Used for periodic house keeping tasks  [" + std::to_string(poll_period_sec_default_m) + "s]\n" +
        "  uid_min=[uint32]    System-assigned credentials minimum UID. Should be >= 1000      [" + std::to_string(sac_uid_min_default_m) + "]\n" +
        "  uid_max=[uint32]    System-assigned credentials maximum UID. Should be > uid_min    [" + std::to_string(sac_uid_max_default_m) + "]\n";

    ctx_p = g_option_context_new(NULL);
    g_option_context_set_summary(ctx_p, "Host Account Management Daemon (hamd)");
    g_option_context_set_description(ctx_p, description.c_str());
    g_option_context_add_main_entries (ctx_p, &options[0], NULL);
    g_option_context_parse (ctx_p, &argc, &argv, NULL);
    g_option_context_free (ctx_p);

    reload();
}

/**
 * @brief Convert a "string" to an integer value. Handles overflow and/or
 *        underflow.
 *
 * @param str_p   The string to convert
 * @param minval  Minimum acceptable value
 * @param maxval  Maximum acceptable value
 * @param err_p   A place where to return an error string indicating why
 *                the function failed.
 *
 * @return str_p converted to a long long. On failure 0 is returned.
 */
long long numberize(const char  * str_p,
                    long long     minval,
                    long long     maxval,
                    const char ** errstr_pp = NULL)
{
    #define OK       0
    #define INVALID  1
    #define TOOSMALL 2
    #define TOOLARGE 3

    struct
    {
        const char * str;
        int          err;
    } table[] =
    {
        { NULL,        errno  }, // preserve current errno
        { "invalid",   EINVAL },
        { "too small", ERANGE },
        { "too large", ERANGE }
    };

    long long    number = 0;
    unsigned     result = OK;
    if (minval > maxval)
    {
        result = INVALID;
    }
    else
    {
        char  * ep;
        errno = 0;
        number = strtoll(str_p, &ep, 10);
        if (str_p == ep || *ep != '\0')
            result = INVALID;
        else if ((number == LLONG_MIN && errno == ERANGE) || number < minval)
            result = TOOSMALL;
        else if ((number == LLONG_MAX && errno == ERANGE) || number > maxval)
            result = TOOLARGE;
    }

    if (errstr_pp != NULL) *errstr_pp = table[result].str;
    errno = table[result].err;

    return result != OK ? 0 : number;
}

/**
 * @brief Read configuration and update hamd_config_c object
 */
void hamd_config_c::reload()
{
    FILE * file = fopen(conf_file_pm, "re");
    if (file)
    {
        gint poll_period_sec = poll_period_sec_default_m;
        gint sac_uid_min     = sac_uid_min_default_m;
        gint sac_uid_max     = sac_uid_max_default_m;
        bool tron            = tron_default_m;

        #define WHITESPACE " \t\n\r"
        char    line[LINE_MAX];
        char  * p;
        char  * s;
        while (NULL != (p = fgets(line, sizeof line, file)))
        {
            p += strspn(p, WHITESPACE);            // Remove leading newline and spaces
            if (*p == '#' || *p == '\0') continue; // Skip comments and empty lines
            p[strcspn(p, "\n\r")] = '\0';          // Remove trailing newline chars

            if (NULL != (s = startswith(p, "debug")))
            {
                s += strspn(s, " \t=");            // Skip leading spaces and equal sign (=)
                tron = strneq(s, "yes", 3);
            }
            else if (NULL != (s = startswith(p, "poll_period")))
            {
                s += strspn(s, " \t=");            // Skip leading spaces and equal sign (=)
                const char * errstr_p = NULL;
                poll_period_sec = (gint)numberize(s, 0, G_MAXINT, &errstr_p);
                if (errstr_p != NULL)
                {
                    sd_journal_print(LOG_ERR, "Error reading %s: poll_period %s (ignored)", conf_file_pm, errstr_p);
                }
            }
            else if (NULL != (s = startswith(p, "uid_min")))
            {
                s += strspn(s, " \t=");            // Skip leading spaces and equal sign (=)
                const char * errstr_p = NULL;
                sac_uid_min = (gint)numberize(s, 1000, G_MAXUINT, &errstr_p);
                if (errstr_p != NULL)
                {
                    sd_journal_print(LOG_ERR, "Error reading %s: uid_min %s (ignored)", conf_file_pm, errstr_p);
                }
            }
            else if (NULL != (s = startswith(p, "uid_max")))
            {
                s += strspn(s, " \t=");            // Skip leading spaces and equal sign (=)
                const char * errstr_p = NULL;
                sac_uid_max = (gint)numberize(s, 1000, G_MAXUINT, &errstr_p);
                if (errstr_p != NULL)
                {
                    sd_journal_print(LOG_ERR, "Error reading %s: uid_max %s (ignored)", conf_file_pm, errstr_p);
                }
            }
        }

        fclose(file);

        tron_m            = tron;
        poll_period_sec_m = poll_period_sec;

        if (sac_uid_min > sac_uid_max)
        {
            sd_journal_print(LOG_ERR, "Error reading %s: uid_max is less than uid_min", conf_file_pm);
        }
        else if ((1 + (sac_uid_max - sac_uid_min)) < 200)
        {
            sd_journal_print(LOG_ERR, "Error reading %s: uid_min..uid_max range too small (should be >= 200).", conf_file_pm);
        }
        else
        {
            sac_uid_min_m   = sac_uid_min;
            sac_uid_max_m   = sac_uid_max;
            sac_uid_range_m = 1 + (sac_uid_max_m - sac_uid_min_m);
        }
    }

    LOG_CONDITIONAL(tron_m, LOG_DEBUG,
                    "hamd_config_c::reload() - conf_file_pm=\"%s\"\n"
                    "  tron_m            = %s\n"
                    "  poll_period_sec_m = %ds\n"
                    "  sac_uid_min_m     = %d\n"
                    "  sac_uid_max_m     = %d\n"
                    "  sac_uid_range_m   = %d\n",
                    conf_file_pm, true_false(tron_m), poll_period_sec_m,
                    sac_uid_min_m, sac_uid_max_m, sac_uid_range_m);
}
