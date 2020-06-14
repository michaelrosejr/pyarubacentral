#!/usr/bin/env python3
"""
This is an example of how to use the following pyarubacentral module.
The sample script includes how to read a config file, access the modules
using a sessiondata refreshing that token and printing the result.
"""
import requests
import json
import click
import time, datetime
import yaml
import logging
import os.path
import sys


from pyarubacentral import auth
import pyarubacentral.get_switches as switches
import pyarubacentral.get_groups as groups
import pyarubacentral.get_networks as networks
import pyarubacentral.get_template_vars as template_vars
import pyarubacentral.get_devices as get_devices
import pyarubacentral.wireless as wireless
from pyarubacentral import monitoring
from pyarubacentral import configuration
from pyarubacentral import device_inventory

from authlib.client import OAuth2Session



#from pyarubacentral import usermgmt


__author__ = "Michael Rose Jr."
__maintainer__ = "Michael Rose Jr."
__email__ = "michael@michaelrosejr.com"
__status__ = "Production"

def read_config():
    with open("config.yml", 'r') as ymlfile:
        data = yaml.load(ymlfile)
    return data


# Read config file
config = read_config()
client_id = config["client_id"]
client_secret = config["client_secret"]
username = config["username"]
password = config["password"]
tokenfile = config["tokenfile"]
baseurl = config["url"]
# if config["envapi"] == "prod":
#     baseurl = "https://app1-apigw.central.arubanetworks.com"
# elif config["envapi"] == "prod2":
#     baseurl = "https://apigw-prod2.central.arubanetworks.com"
# else:
#     baseurl = "https://internal-apigw.central.arubanetworks.com"

current_time = time.time() * 1000


def get_new_access_token(config):

    #print(config)
    cookies = dict(auth.CentralAuth.central_login(config))
    # print(cookies)
    auth_code = json.loads(auth.CentralAuth.get_auth_code_v2(cookies, config))
    # print(auth_code['auth_code'])
    session = json.loads(auth.CentralAuth.get_access_tokens(config, auth_code['auth_code']))

    session['created_at'] = current_time
    print(session)
    with open(tokenfile, "w") as savetoken:
        json.dump(session, savetoken)

    return session

if os.path.isfile(tokenfile):
    with open(tokenfile) as exjsonfile:
        sessiondata = json.load(exjsonfile)

    # print(sessiondata)
    # if(sessiondata['error_description'] == 'Invalid client authentication')
    #     auth.get_auth_code('')

    check_refresh_token = sessiondata.get('refresh_token')
    # check_refresh_token = None
    #check_refresh_token = None
    if check_refresh_token is not None:
        refresh_token = sessiondata["refresh_token"]
        # sessiondata = sessiondata["sessiondata"]
        created_at = sessiondata["created_at"]
        expires_in = sessiondata["expires_in"]
        expires_at = ((created_at / 1000) + expires_in) * 1000
        sessiondata["baseurl"] = baseurl


        if current_time  > expires_at:
            print("Refreshing token")
            url = baseurl + "/oauth2/token"
            payload = {'refresh_token': refresh_token, 'client_id': client_id, 'client_secret': client_secret,
                       'grant_type': 'refresh_token'}
            response = requests.post(url, params=payload)
            tokenconfig = response.json()
            tokenconfig['created_at'] = current_time
            with open(tokenfile, "w") as exjsonfile:
                json.dump(tokenconfig, exjsonfile)
    else:
        cookies = dict(auth.CentralAuth.get_login_cookies(config))
        logging.info(cookies)
        csrf_token = json.loads(auth.CentralAuth.get_csrf_token(cookies, config, client_id))
        logging.info("CSRF Token", csrf_token)
        auth_code = json.loads(auth.CentralAuth.get_auth_code(cookies, config))
        logging.info("AUTHCODE", auth_code)
        tokens = auth.CentralAuth.get_access_tokens(config, auth_code['auth_code'])
        logging.info("tokens: ",tokens)
        tokenconfig = json.loads(tokens)
        tokenconfig['created_at'] = current_time
        # print(tokenconfig)
        with open(tokenfile, "w") as exjsonfile:
            json.dump(tokenconfig, exjsonfile)

else:

    sessiondata = get_new_access_token(config)




@click.group()
def cli():
    """CLI for Aruba Central"""
    pass

# @cli.command()
# @click.option('--refresh', flag_value=1)
# def app(grouplist, networklist, refresh, group, templatevars):
#
#     if refresh:
#         url = "https://app1-apigw.central.arubanetworks.com/oauth2/token"
#         payload = {'refresh_token': refresh_token, 'client_id': client_id, 'client_secret': client_secret, 'grant_type': 'refresh_token' }
#         response = requests.post(url, params=payload)
#         tokenconfig = response.json()
#         tokenconfig['created_at'] = current_time() + tokenconfig['expires_in']
#         # with open(tokenfile, "w") as exjsonfile:
#         #     json.dump(response.json(), exjsonfile)

@cli.command()
@click.option('--serial', '-s', required=True, help="Create device template vars for device")
@click.option('--jsonfile', '-j', required=True, help="JSON file to add to Central")
def create_device_vars(serial, jsonfile):
    # create_device = configuration.Configuration(sessiondata, serial, jsonfile)
    # print(create_device.get_configuration_v1_devices_template_variables())
    # print("{\"Response\": \"Successful\"}")
    pass

@cli.command()
@click.option('--serial', '-s', help="Get templates vars for device", required=True)
def get_configuration_template_vars(serial):
    device_vars = configuration.Configuration(sessiondata, serial, 'none')
    print(device_vars.get_configuration_v1_devices_template_variables())

@cli.command()
@click.option('--type', help="Get Devices", required=True)
def get_devices(type):
    print(device_inventory.DeviceInventory.get_devices(sessiondata, type))

@cli.command()
def get_monitoring_net():
    print((monitoring.Monitoring.get_monitoring_v1_networks(sessiondata)))

@cli.command()
def get_monitoring_switches():
    networklist = monitoring.Monitoring(sessiondata, 'none')
    print(networklist.get_monitoring_v1_switches())

@cli.command()
def get_bssids():
    bssids = monitoring.Monitoring(sessiondata, 'none')
    print(bssids.get_monitoring_v1_bssids())

# @cli.command()
# def get_accounts_v2_users():
#     v2_users = usermgmt.Usermgmt(sessiondata, 'none')
#     print(v2_users.get_accounts_v2_users())
#
# @cli.command()
# def get_accounts_v1_roles():
#     v1_roles = usermgmt.Usermgmt(sessiondata, 'none')
#     print(v1_roles.get_accounts_v1_roles())


# @cli.command()
# def templatevars():
#     print(json.dumps((template_vars.get_template_vars(sessiondata, templatevars))))

@cli.command()
def switchlist():
    print(json.dumps((switches.get_switches(sessiondata))))

@cli.command()
def switchdetails():
    print(json.dumps((switches.get_switch_detials(sessiondata, 'CN76JYL0BQ'))))

@cli.command()
def check_version_switches():
    switchinv=((get_devices.get_device_inventory(sessiondata, 'MAS')))
    # print(switchinv['devices'])
    slist = []
    for eachswitch in switchinv['devices']:
        # print(eachswitch['serial'])
        slist.append(switches.get_switch_detials(sessiondata, eachswitch['serial']))
    print(json.dumps(slist))

@cli.command()
def switch_inventory():
    print(json.dumps((get_devices.get_device_inventory(sessiondata, 'MAS'))))

@cli.command()
def get_wifi_clients():
    print(json.dumps((wireless.get_wifi_clients(sessiondata, 'USOC'))))

@cli.command()
def get_wifi_aps():
    print(json.dumps((wireless.get_wifi_aps(sessiondata, 'USOC'))))

@cli.command()
def get_wifi_ble():
    print(json.dumps((wireless.get_ble_addr(sessiondata))))


@cli.command()
def networklist():
    print(json.dumps((networks.get_networks(sessiondata))))

@cli.command()
def grouplist():
    print(json.dumps((groups.get_groups(sessiondata))))

@cli.command()
@click.option('--groupname', help="Enter group name to search")
def group(groupname):
    #groupname = "Retail_AMER"
    print(json.dumps((groups.get_group(sessiondata, groupname))))

@cli.command()
def get_centraljson():
    print(centraljson.get_centraljson(sessiondata))


@cli.command()
def push_ap():
    apdata = {
        "mac": "04:bd:33:e1:33:33",
        "serial": "CX0001589"
    }
    # print(json.dumps(apdata))
    # print(sessiondata)
    url = "https://apigw-prod2.central.arubanetworks.com/device_inventory/v2/devices"
    atoken = {'access_token': sessiondata['access_token']}
    headers = {"Accept": "application/json"}
    payload = {**atoken, **apdata}
    print(payload)
    try:
        r = requests.post(url, params=payload, headers=headers)
        # r.raise_for_status()
        if r.status_code != 200:
            print('Status:', r.status_code, '\nHeaders:', r.headers,
                    '\nError Response:', r.text)
        return r.text
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)

@cli.command()
def donothing():
    pass

if __name__ == "__main__":
    cli()
