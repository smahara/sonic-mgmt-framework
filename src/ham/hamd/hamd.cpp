// Host Account Management
#include <glib.h>               // g_file_test()
#include <glib/gstdio.h>        // g_chdir()
#include <stdio.h>
#include <stdlib.h>             // system()
#include <sys/types.h>          // getpwnam(), getpid()
#include <pwd.h>                // fgetpwent()
#include <string>               // std::string
#include <sstream>              // std::ostringstream
#include <systemd/sd-journal.h> // sd_journal_print()
#include <pwd.h>                // getpwnam(), getpwuid()
#include <grp.h>                // getgrnam(), getgrgid()
#include <shadow.h>             // getspnam()
#include <unistd.h>             // getpid()

#include "hamd.h"               // hamd_c
#include "../shared/utils.h"    // startswith()
#include "siphash24.h"          // siphash24()

/**
 * @brief DBus adaptor class constructor
 *
 * @param config_r Structure containing configuration parameters
 * @param conn_r
 */
hamd_c::hamd_c(hamd_config_c & config_r, DBus::Connection & conn_r) :
    DBus::ObjectAdaptor(conn_r, DBUS_OBJ_PATH_BASE),
    config_rm(config_r),
    poll_timer_m((double)config_rm.poll_period_sec_m, hamd_c::on_poll_timeout, this)
{
    apply_config();
}

/**
 * @brief This is called when the poll_timer_m expires.
 *
 * @param user_data_p Pointer to user data. In this case this point to the
 *                    hamd_c object.
 * @return bool
 */
bool hamd_c::on_poll_timeout(gpointer user_data_p)
{
    hamd_c * p = static_cast<hamd_c *>(user_data_p);
    LOG_CONDITIONAL(p->is_tron(), LOG_INFO, "hamd_c::on_poll_timeout()");
    p->rm_unconfirmed_users();
    return true; // Return true to repeat timer
}

/**
 * @brief reload configuration and apply to running daemon.
 */
void hamd_c::reload()
{
    LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "hamd_c::reload()");
    config_rm.reload();
    apply_config();
}

/**
 * @brief Apply the configuration to the running daemon
 */
void hamd_c::apply_config()
{
    if (config_rm.poll_period_sec_m > 0)
        poll_timer_m.start((double)config_rm.poll_period_sec_m);
    else
        poll_timer_m.stop();
}

/**
 * @brief This is called just before the destructor is called and is used
 *        to clean up all resources in use by the class instance.
 */
void hamd_c::cleanup()
{
    poll_timer_m.stop();
}

/**
 * @brief Create a new user
 */
int32_t hamd_c::useradd(const std::string& login, const std::string& options)
{
    return 0;
}

/**
 * @brief Modify a user account
 */
int32_t hamd_c::usermod(const std::string& login, const std::string& options)
{
    return 0;
}

/**
 * @brief Create a new group
 */
int32_t hamd_c::groupadd(const std::string& group, const std::string& options)
{
    return 0;
}

/**
 * @brief Modify a group definition on the system
 */
int32_t hamd_c::groupmod(const std::string& group, const std::string& options)
{
    return 0;
}

::DBus::Struct< bool, std::string, std::string, uint32_t, uint32_t, std::string, std::string, std::string > hamd_c::getpwnam(const std::string& name)
{
    ::DBus::Struct< bool,         /* success   */
                    std::string,  /* pw_name   */
                    std::string,  /* pw_passwd */
                    uint32_t,     /* pw_uid    */
                    uint32_t,     /* pw_gid    */
                    std::string,  /* pw_gecos  */
                    std::string,  /* pw_dir    */
                    std::string > /* pw_shell  */ ret;

    LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "hamd_c::getpwnam(%s)", name.c_str());

    struct passwd * p = ::getpwnam(name.c_str());

    ret._1 = p != NULL;
    if (ret._1) // success?
    {
        ret._2 = p->pw_name;
        ret._3 = p->pw_passwd;
        ret._4 = p->pw_uid;
        ret._5 = p->pw_gid;
        ret._6 = p->pw_gecos;
        ret._7 = p->pw_dir;
        ret._8 = p->pw_shell;
    }

    return ret;
}

::DBus::Struct< bool, std::string, std::string, uint32_t, uint32_t, std::string, std::string, std::string > hamd_c::getpwuid(const uint32_t& uid)
{
    ::DBus::Struct< bool,         /* success   */
                    std::string,  /* pw_name   */
                    std::string,  /* pw_passwd */
                    uint32_t,     /* pw_uid    */
                    uint32_t,     /* pw_gid    */
                    std::string,  /* pw_gecos  */
                    std::string,  /* pw_dir    */
                    std::string > /* pw_shell  */ ret;

    LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "hamd_c::getpwuid(%u)", uid);

    struct passwd * p = ::getpwuid(uid);

    ret._1 = p != NULL;
    if (ret._1) // success?
    {
        ret._2 = p->pw_name;
        ret._3 = p->pw_passwd;
        ret._4 = p->pw_uid;
        ret._5 = p->pw_gid;
        ret._6 = p->pw_gecos;
        ret._7 = p->pw_dir;
        ret._8 = p->pw_shell;
    }

    return ret;
}

::DBus::Struct< bool, std::string, std::string, uint32_t, std::vector< std::string > > hamd_c::getgrnam(const std::string& name)
{
    ::DBus::Struct< bool,                        /* success   */
                    std::string,                 /* gr_name   */
                    std::string,                 /* gr_passwd */
                    uint32_t,                    /* gr_gid    */
                    std::vector< std::string > > /* gr_mem    */ ret;

    LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "hamd_c::getgrnam(%s)", name.c_str());

    struct group * p = ::getgrnam(name.c_str());

    ret._1 = p != NULL;
    if (ret._1) // success?
    {
        ret._2 = p->gr_name;
        ret._3 = p->gr_passwd;
        ret._4 = p->gr_gid;

        for (unsigned i = 0; p->gr_mem[i] != NULL; i++)
            ret._5.push_back(p->gr_mem[i]);
    }

    return ret;
}

::DBus::Struct< bool, std::string, std::string, uint32_t, std::vector< std::string > > hamd_c::getgrgid(const uint32_t& gid)
{
    ::DBus::Struct< bool,                        /* success   */
                    std::string,                 /* gr_name   */
                    std::string,                 /* gr_passwd */
                    uint32_t,                    /* gr_gid    */
                    std::vector< std::string > > /* gr_mem    */ ret;

    LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "hamd_c::getgrgid(%u)", gid);

    struct group * p = ::getgrgid(gid);

    ret._1 = p != NULL;
    if (ret._1) // success?
    {
        ret._2 = p->gr_name;
        ret._3 = p->gr_passwd;
        ret._4 = p->gr_gid;

        for (unsigned i = 0; p->gr_mem[i] != NULL; i++)
            ret._5.push_back(p->gr_mem[i]);
    }

    return ret;
}

::DBus::Struct< bool, std::string, std::string, int32_t, int32_t, int32_t, int32_t, int32_t, int32_t, uint32_t > hamd_c::getspnam(const std::string& name)
{
    ::DBus::Struct< bool,        /* success   */
                    std::string, /* sp_namp   */
                    std::string, /* sp_pwdp   */
                    int32_t,     /* sp_lstchg */
                    int32_t,     /* sp_min    */
                    int32_t,     /* sp_max    */
                    int32_t,     /* sp_warn   */
                    int32_t,     /* sp_inact  */
                    int32_t,     /* sp_expire */
                    uint32_t >   /* sp_flag   */ ret;

    LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "hamd_c::getspnam(%s)", name.c_str());

    struct spwd * p = ::getspnam(name.c_str());

    ret._1 = p != NULL;
    if (ret._1) // success?
    {
        ret._2  = p->sp_namp;
        ret._3  = p->sp_pwdp;
        ret._4  = p->sp_lstchg;
        ret._5  = p->sp_min;
        ret._6  = p->sp_max;
        ret._7  = p->sp_warn;
        ret._8  = p->sp_inact;
        ret._9  = p->sp_expire;
        ret._10 = p->sp_flag;
    }

    return ret;
}

/**
 * @brief Remove unconfirmed users from /etc/passwd. Unconfirmed users have
 *        the string "Unconfirmed sac user [PID]" in their GECOS string and
 *        the PID does not exist anymore.
 */
void hamd_c::rm_unconfirmed_users() const
{
    FILE  * f = fopen("/etc/passwd", "re");
    if (f)
    {
        struct passwd * ent;
        std::string     base_cmd("/usr/sbin/userdel --remove ");
        std::string     full_cmd;
        g_chdir("/proc");
        while (NULL != (ent = fgetpwent(f)))
        {
            const char * pid_p;
            if ((ent->pw_uid >= (uid_t)config_rm.sac_uid_min_m) && (ent->pw_uid <= (uid_t)config_rm.sac_uid_max_m) &&
                (NULL != (pid_p = startswith(ent->pw_gecos, "Unconfirmed system-assigned credentials "))))
            {
                if (!g_file_test(pid_p, G_FILE_TEST_EXISTS))
                {
                    // Directory does not exist, which means process does not
                    // exist either. Let's remove this user which was never
                    // confirmed by PAM authentification.
                    full_cmd = base_cmd + ent->pw_name;
                    int ret = system(full_cmd.c_str());
                    if (!WIFEXITED(ret) || (WEXITSTATUS(ret) != 0))
                    {
                        sd_journal_print(LOG_ERR, "User \"%s\": Failed to removed unconfirmed user UID=%d",
                                         ent->pw_name, ent->pw_uid);
                    }
                }
            }
        }
        fclose(f);
    }
}

/**
 * @brief This is a DBus interface used by remote programs to add an
 *        unconfirmed user.
 *
 * @param username  Username to be added
 * @param pid       PID of the caller.
 *
 * @return bool     true if user was added successfully,
 *                  false otherwise.
 */
bool hamd_c::add_unconfirmed_user(const std::string& username, const uint32_t& pid)
{
    // First, let's check if there are any
    // unconfirmed users that could be removed.
    rm_unconfirmed_users();

    // Next, add <username> as an unconfirmed user.
    static const uint8_t hash_key[] =
    {
        0x37, 0x53, 0x7e, 0x31, 0xcf, 0xce, 0x48, 0xf5,
        0x8a, 0xbb, 0x39, 0x57, 0x8d, 0xd9, 0xec, 0x59
    };

    unsigned     n_tries;
    uid_t        candidate;
    std::string  name(username);
    std::string  full_cmd;
    std::string  base_cmd = "/usr/sbin/useradd"
                            " --create-home"
                            " --no-user-group"
                            " --shell /usr/bin/klish"
                            " --user-group"
                            " --comment \"Unconfirmed system-assigned credentials " + std::to_string(pid) + '"';

    for (n_tries = 0; n_tries < 100; n_tries++) /* Give up retrying eventually */
    {
        // Find a unique UID in the range sac_uid_min_m..sac_uid_max_m.
        // We use a hash function to always get the same ID for a given user
        // name. Hash collisions (i.e. two user names with the same hash) will
        // be handled by trying with a slightly different username.
        candidate = config_rm.uid_fit_into_range(siphash24(name.c_str(), name.length(), hash_key));

        LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "User \"%s\": attempt %d using name \"%s\", candidate UID=%lu",
                        username.c_str(), n_tries, name.c_str(), (unsigned long)candidate);

        // Note: The range 60000-64999 is reserved on Debian platforms
        //       and should be avoided and the value 65535 is traditionally
        //       reserved as an "error" code.
        if (!((candidate >= 60000) && (candidate <= 64999)) &&
             (candidate != 65535) &&
            !::getpwuid(candidate)) /* make sure not already allocated */
        {
            full_cmd = base_cmd + " --uid " + std::to_string(candidate) + ' ' + username;

            LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "User \"%s\": executing \"%s\"", username.c_str(), full_cmd.c_str());

            int  rc          = system(full_cmd.c_str());
            bool term_normal = WIFEXITED(rc);
            int  exit_status = WEXITSTATUS(rc);

            LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "User \"%s\": command returned term_normal=%s, exit_status=%d, errno=%d (%s)",
                            username.c_str(), term_normal ? "true" : "false", exit_status, errno, strerror(errno));

            return term_normal && (0 == exit_status) ? true : false;
        }
        else
        {
            // Try with a slightly different name
            name = username + std::to_string(n_tries);
            LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "User \"%s\": candidate UID=%lu already in use. Retry with name = \"%s\"",
                            username.c_str(), (unsigned long)candidate, name.c_str());
        }
    }

    sd_journal_print(LOG_ERR, "User \"%s\": unable to create unconfirmed user after %d attempts",
                     username.c_str(), n_tries);

    return false;
}

/**
 * @brief  Generate ssh keys
 *
 * @param  username_p   user name
 *
 * @return true if successful, false otherwise.
 */
static bool generate_certs(const std::string username)
{
    static const char * fname_p = "/usr/bin/certgen";
    if (!g_file_test(fname_p, G_FILE_TEST_EXISTS))
        return false;

    std::string cmd         = "/bin/sh " + (fname_p + (' ' + username));
    int         ret         = system(cmd.c_str());
    bool        term_normal = WIFEXITED(ret);
    int         exit_status = WEXITSTATUS(ret);
    bool        ok          = term_normal && (exit_status == 0) ? true : false;

    if (!ok)
    {
        sd_journal_print(LOG_ERR, "User %s: Failed to run \"%s\". term_normal=%s, exit_status=%d, errno=%d (%s)",
                         username.c_str(), cmd.c_str(), term_normal ? "true" : "false", exit_status,
                         errno, strerror(errno));
    }

    return ok;
}

/**
 * @brief This is a DBus interface used by remote programs to confirm a
 *        user.
 *
 * @param username  Username to be confirmed
 * @param groupname User's Primary group
 * @param groups    User's Supplementory groups (comma-separated list)
 * @param label     Label to be added in the comment (e.g. "RADIUS",
 *                  "TACACS+", "AAA", etc...)
 *
 * @return bool     true if user was confirmed successfully,
 *                  false otherwise.
 */
bool hamd_c::confirm_user(const std::string& username, const std::string& groupname, const std::string& groups, const std::string& label)
{
    std::string  cmd("/usr/sbin/usermod --comment \"Automagic user");

    if (label.length() != 0)
        cmd += ' ' + label;

    cmd += '"';

    if (groups.length() != 0)
        cmd += " --append --groups " + groups;

    cmd += " --gid " + groupname + ' ' + username;

    LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "User \"%s\": executing \"%s\"", username.c_str(), cmd.c_str());

    int  rc          = system(cmd.c_str());
    bool term_normal = WIFEXITED(rc);
    int  exit_status = WEXITSTATUS(rc);

    LOG_CONDITIONAL(is_tron(), LOG_DEBUG, "User \"%s\": command returned term_normal=%s, exit_status=%d, errno=%d (%s)",
                    username.c_str(), term_normal ? "true" : "false", exit_status, errno, strerror(errno));

    bool ok = term_normal && (0 == exit_status);

    if (ok)
        ok = generate_certs(username);

    return ok;
}

/**
 * @brief This is a DBus interface used to turn tracing on. This allows
 *        the daemon to run with verbosity turned on.
 *
 * @return std::string
 */
std::string hamd_c::tron()
{
    config_rm.tron_m = true;
    return "Tracing is now ON";
}

/**
 * @brief This is a DBus interface used to turn tracing off. This allows
 *        the daemon to run with verbosity turned off.
 *
 * @return std::string
 */
std::string hamd_c::troff()
{
    config_rm.tron_m = false;
    return "Tracing is now OFF";
}

/**
 * @brief This is a DBus interface used to retrieve daemon running info
 *
 * @return std::string
 */
std::string hamd_c::show()
{
    std::ostringstream  dbg;
    dbg << "PID               = " << getpid() << '\n'
        << "conf_file_pm      = " << config_rm.conf_file_pm << '\n'
        << "tron_m            = " << (config_rm.tron_m ? "true" : "false") << '\n'
        << "poll_period_sec_m = " << std::to_string(config_rm.poll_period_sec_m)  << "s\n"
        << "poll_timer_m      = " << poll_timer_m << '\n'
        << "sac_uid_min_m     = " << std::to_string(config_rm.sac_uid_min_m)  << '\n'
        << "sac_uid_max_m     = " << std::to_string(config_rm.sac_uid_max_m)  << '\n'
        << "sac_uid_range_m   = " << std::to_string(config_rm.sac_uid_range_m)  << '\n';

    return dbg.str();
}
