import getpass
import os
API_KEY_PATH = "/etc/rest_api_keys"

def set_api_key(config):
    username = getpass.getuser()
    config.api_key_prefix['X-API-Key'] = username
    config.api_key['X-API-Key'] = open(os.path.join(API_KEY_PATH, "{}.key".format(username))).read().strip()