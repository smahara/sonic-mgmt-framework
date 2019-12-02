// Host Account Management
#include <glib.h>               // g_file_test()
#include <glib/gstdio.h>        // g_chdir()
#include <stdio.h>
#include <stdlib.h>             // system()
#include <sys/types.h>          // getpwnam()
#include <pwd.h>                // fgetpwent()
#include <string>               // std::string
#include <sstream>              // std::ostringstream
#include <systemd/sd-journal.h> // sd_journal_print()
#include <pwd.h>                // getpwnam(), getpwuid()
#include <grp.h>                // getgrnam(), getgrgid()
#include <shadow.h>             // getspnam()

#include "hamd.h"               // hamd_c
#include "../shared/utils.h"     // startswith()

/**
 * @brief DBus adaptor class constructor
 *
 * @param config_r Structure containing configuration parameters
 * @param conn_r
 */
hamd_c::hamd_c(const config_c & config_r, DBus::Connection & conn_r) :
    DBus::ObjectAdaptor(conn_r, DBUS_OBJ_PATH_BASE),
    tron_m(config_r.verbose_m)
{
}

/**
 * @brief This is called just before the destructor is called and is used
 *        to clean up all resources in use by the class instance.
 */
void hamd_c::cleanup()
{
}

int32_t hamd_c::useradd(const std::string& login, const std::string& options)
{
    return 0;
}

int32_t hamd_c::usermod(const std::string& login, const std::string& options)
{
    return 0;
}

int32_t hamd_c::groupadd(const std::string& group, const std::string& options)
{
    return 0;
}

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
 * @brief This is a DBus interface used to turn tracing on. This allows
 *        the daemon to run with verbosity turned on.
 *
 * @return std::string
 */
std::string hamd_c::tron()
{
    tron_m = true;
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
    tron_m = false;
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

    dbg << "tron_m       = " << (tron_m ? "true" : "false") << '\n';

    return dbg.str();
}
