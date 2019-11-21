// Host Account Management
#include <glib.h>                       // g_main_loop_new(), g_main_context_default(), g_main_loop_run(), g_main_loop_unref(), g_main_loop_quit(), gboolean, etc...
#include <glib-unix.h>                  // g_unix_signal_add()
#include <dbus-c++/glib-integration.h>  // DBus::Glib::BusDispatcher, DBus::default_dispatcher
#include <stdlib.h>                     // EXIT_SUCCESS, EXIT_FAILURE
#include <systemd/sd-journal.h>         // sd_journal_print()

#include "hamd.h"                       // hamd_c

inline const char * true_false          (bool x, const char * pos_p = "true", const char * neg_p = "false")   { return (x) ? pos_p : neg_p; }

/**
 * @brief Parse command-line options/arguments
 *
 */
config_c::config_c(int argc, char **argv)
{
    GOptionContext  * context_p;
    std::string       poll_help    = "Main loop polling period [" + std::to_string(poll_period_sec_m) + "s]";
    std::string       min_uid_help = "Minimum UID              [" + std::to_string(sac_uid_min_m) + ']';
    std::string       max_uid_help = "Maximum UID              [" + std::to_string(sac_uid_max_m) + ']';
    std::string       verbose_help = "Print extra debug        [" + std::string(true_false(verbose_m)) + ']';

    static const GOptionEntry options[] =
    {
        { "poll-period", 'p',  G_OPTION_FLAG_NONE, G_OPTION_ARG_INT,  &poll_period_sec_m, poll_help.c_str(),    NULL },
        { "min-uid",     'm',  G_OPTION_FLAG_NONE, G_OPTION_ARG_INT,  &sac_uid_min_m,     min_uid_help.c_str(), NULL },
        { "max-uid",     'M',  G_OPTION_FLAG_NONE, G_OPTION_ARG_INT,  &sac_uid_max_m,     max_uid_help.c_str(), NULL },
        { "verbose",     'v',  G_OPTION_FLAG_NONE, G_OPTION_ARG_NONE, &verbose_m,         verbose_help.c_str(), NULL },
        { NULL,          '\0', G_OPTION_FLAG_NONE, G_OPTION_ARG_NONE, NULL,               NULL,                 NULL }
    };

    context_p = g_option_context_new (NULL);
    g_option_context_set_summary (context_p, "Host Account Management Daemon (hamd)");
    g_option_context_add_main_entries (context_p, &options[0], NULL);
    g_option_context_parse (context_p, &argc, &argv, NULL);
    g_option_context_free (context_p);
}

/**
 * @brief This callback will be invoked when this process receives SIGINT
 *        or SIGTERM.
 *
 * @param data
 *
 * @return gboolean
 */
static gboolean terminationSignalCallback(gpointer data)
{
    GMainLoop * loop_p = static_cast<GMainLoop *>(data);
    g_main_loop_quit(loop_p);
    return FALSE;
}

/**
 * @brief Program entry point
 *
 * @param argc
 * @param argv
 *
 * @return int
 */
int main(int argc, char *argv[])
{
    setvbuf(stdout, NULL, _IONBF, 0); // Set stdout buffering to unbuffered

    //putenv("DBUSXX_VERBOSE=1");

    config_c  config(argc, argv);

    sd_journal_print(LOG_DEBUG, "Creating a GMainLoop");
    GMainContext * main_ctx_p = g_main_context_default();
    GMainLoop    * loop_p     = g_main_loop_new(main_ctx_p, FALSE);

    // Set up a signal handler for handling SIGINT and SIGTERM.
    g_unix_signal_add(SIGINT,  terminationSignalCallback, loop_p); // CTRL-C
    g_unix_signal_add(SIGTERM, terminationSignalCallback, loop_p); // systemctl stop

    // DBus setup
    sd_journal_print(LOG_DEBUG, "Initializing the loop's dispatcher");
    DBus::Glib::BusDispatcher   dispatcher;
    DBus::default_dispatcher = &dispatcher;
    dispatcher.attach(main_ctx_p);

    sd_journal_print(LOG_DEBUG, "Requesting System DBus connection \"" DBUS_BUS_NAME_BASE "\"");
    DBus::Connection  dbus_conn(DBus::Connection::SystemBus());
    dbus_conn.request_name(DBUS_BUS_NAME_BASE);

    hamd_c  hamd(config, dbus_conn); // DBus handlers

    sd_journal_print(LOG_DEBUG, "Entering main loop");
    g_main_loop_run(loop_p);

    hamd.cleanup();

    sd_journal_print(LOG_DEBUG, "Cleaning up and exiting");
    g_main_loop_unref(loop_p);

    sd_journal_print(LOG_DEBUG, "Exiting daemon.");

    fflush(stdout);

    exit(EXIT_SUCCESS);
}

