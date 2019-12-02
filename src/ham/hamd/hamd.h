// Host Account Management
#ifndef HAMD_H
#define HAMD_H

#include <dbus-c++/dbus.h>          // DBus::Connection
#include <glib.h>                   // gboolean, gpointer
#include "../shared/dbus-address.h" // DBUS_BUS_NAME_BASE

#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wunused-but-set-variable"   /* SUPPRESS: warning: variable 'ri' set but not used [-Wunused-but-set-variable] */
#include "../shared/org.SONiC.HostAccountManagement.dbus-adaptor.h"
#pragma GCC diagnostic pop

class config_c
{
public:
    config_c(int argc, char **argv);
    bool  verbose_m = false;
};

class hamd_c : public DBus::ObjectAdaptor,
               public DBus::IntrospectableAdaptor,
               public ham::accounts_adaptor,
               public ham::name_service_adaptor,
               public ham::debug_adaptor
{
public:
    hamd_c(const config_c & config_r, DBus::Connection  & conn_r);
    virtual ~hamd_c() {}

    // DBus "accounts" interface
    virtual int32_t useradd(const std::string& login, const std::string& options);
    virtual int32_t usermod(const std::string& login, const std::string& options);
    virtual int32_t groupadd(const std::string& group, const std::string& options);
    virtual int32_t groupmod(const std::string& group, const std::string& options);

    // DBus "nss" interface
    virtual ::DBus::Struct< bool, std::string, std::string, uint32_t, uint32_t, std::string, std::string, std::string > getpwnam(const std::string& name);
    virtual ::DBus::Struct< bool, std::string, std::string, uint32_t, uint32_t, std::string, std::string, std::string > getpwuid(const uint32_t& uid);
    virtual ::DBus::Struct< bool, std::string, std::string, uint32_t, std::vector< std::string > > getgrnam(const std::string& name);
    virtual ::DBus::Struct< bool, std::string, std::string, uint32_t, std::vector< std::string > > getgrgid(const uint32_t& gid);
    virtual ::DBus::Struct< bool, std::string, std::string, int32_t, int32_t, int32_t, int32_t, int32_t, int32_t, uint32_t > getspnam(const std::string& name);

    // DBus "debug" interface
    virtual std::string  tron();
    virtual std::string  troff();
    virtual std::string  show();

public:
    bool          is_tron() const { return tron_m; }
    virtual void  cleanup();

private:
    bool          tron_m;
};


#define LOG_CONDITIONAL(condition, args...) do { if (condition) {sd_journal_print(args);} } while(0)

#endif /* HAMD_H */
