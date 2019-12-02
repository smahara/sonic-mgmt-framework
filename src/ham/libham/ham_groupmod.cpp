// Host Account Management
#include "ham.h"
#include "dbus-proxy.h"
#include "../shared/dbus-address.h" /* DBUS_BUS_NAME_BASE, DBUS_OBJ_PATH_BASE */

int ham_groupmod(const char * group, const char * options)
{
    DBus::BusDispatcher         dispatcher;
    DBus::default_dispatcher = &dispatcher;
    DBus::Connection conn    = DBus::Connection::SystemBus();

    accounts_proxy_c interface(conn, DBUS_BUS_NAME_BASE, DBUS_OBJ_PATH_BASE);
    return interface.groupmod(group, options != nullptr ? options : "");
}

