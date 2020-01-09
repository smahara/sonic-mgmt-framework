""" Renew DHCP lease handler"""
import host_service
import subprocess

MOD_NAME= 'renew_dhcp_lease'

class RENEW_DHCP_LEASE(host_service.HostModule):
    """DBus endpoint that executes RENEW_DHCP_LEASE related commands """

    @staticmethod
    def _run_command(options):
        """ Run renew dhcp lease command """
        if len(options) < 2:
            print("RENEW_DHCP_LEASE Invalid options, {}".format(options))
            return 1, "Invalid options"

        ifName = options[0]
        version = ""
        file_ext = ""
        cmd_opt = ""
        output = ""
        rc = 0
        try:
            for x in options[1:]:
                if x == "ipv6":
                    version = "-6"
                    file_ext = "6"
                    cmd_opt = "-D LL"

                cmd = "/sbin/dhclient {} -r {}".format(version, ifName)
                print("RENEW_DHCP_LEASE - cmd {}".format(cmd))
                output = subprocess.check_call(cmd, shell=True)
                print('RENEW_DHCP_LEASE release Output -> ', output)

                cmd = "[ -f /var/run/dhclient{}.{}.pid ] && kill `cat /var/run/dhclient{}.{}.pid` && rm -f /var/run/dhclient{}.{}.pid".format(file_ext, ifName, file_ext, ifName, file_ext, ifName)
                print("RENEW_DHCP_LEASE - cmd {}".format(cmd))
                output = subprocess.check_call(cmd, shell=True)
                print('RENEW_DHCP_LEASE release Output -> ', output)

                cmd = "/sbin/dhclient {} -pf /run/dhclient{}.{}.pid -lf /var/lib/dhcp/dhclient{}.{}.leases {} -nw {} ".format(version, file_ext, ifName, file_ext, ifName, ifName, cmd_opt)
                print("RENEW_DHCP_LEASE - cmd {}".format(cmd))
                output = subprocess.check_call(cmd, shell=True)
                print('RENEW_DHCP_LEASE Output -> ', output)

        except subprocess.CalledProcessError as err:
            print("Exception when calling get_sonic_error -> %s\n" %(err))
            rc = err.returncode
            output = err.output
            
        return rc,output


    @host_service.method(host_service.bus_name(MOD_NAME), in_signature='as', out_signature='is')
    def action(self, options):
        return RENEW_DHCP_LEASE._run_command(options)
        
def register():
    """Return class name"""
    return RENEW_DHCP_LEASE, MOD_NAME
