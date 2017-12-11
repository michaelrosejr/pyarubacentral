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

from pyarubacentral import auth
import pyarubacentral.get_switches as switches
import pyarubacentral.get_groups as groups
import pyarubacentral.get_networks as networks
import pyarubacentral.get_template_vars as template_vars
from pyarubacentral import monitoring
from pyarubacentral import configuration
from pyarubacentral import usermgmt

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
tokenfile = config["tokenfile"]
if config["envapi"] == "prod":
    baseurl = "https://app1-apigw.central.arubanetworks.com"
else:
    baseurl = "https://internal-apigw.central.arubanetworks.com"

with open(tokenfile) as exjsonfile:
    sessiondata = json.load(exjsonfile)

current_time = time.time() * 1000

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

@cli.command()
def get_accounts_v2_users():
    v2_users = usermgmt.Usermgmt(sessiondata, 'none')
    print(v2_users.get_accounts_v2_users())

@cli.command()
def get_accounts_v1_roles():
    v1_roles = usermgmt.Usermgmt(sessiondata, 'none')
    print(v1_roles.get_accounts_v1_roles())


# @cli.command()
# def templatevars():
#     print(json.dumps((template_vars.get_template_vars(sessiondata, templatevars))))

@cli.command()
def switchlist():
    print(json.dumps((switches.get_switches(sessiondata))))

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

if __name__ == "__main__":
    cli()
