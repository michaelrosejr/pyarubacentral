#!/usr/bin/env python3
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

def read_config():
    with open("config.yml", 'r') as ymlfile:
        data = yaml.load(ymlfile)
    return data


# Read config file
config = read_config()
client_id = config["client_id"]
client_secret = config["client_secret"]
tokenfile = config["tokenfile"]

with open(tokenfile) as exjsonfile:
    exchange_data = json.load(exjsonfile)

current_time = time.time() * 1000

refresh_token = exchange_data["refresh_token"]
access_token = exchange_data["access_token"]
created_at = exchange_data["created_at"]
expires_in = exchange_data["expires_in"]
expires_at = ((created_at / 1000) + expires_in) * 1000


if current_time  > expires_at:
    print("Refreshing token")
    url = "https://app1-apigw.central.arubanetworks.com/oauth2/token"
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
def get_monitoring_net():
    print((monitoring.Monitoring.get_monitoring_v1_networks(access_token, refresh_token)))

@cli.command()
def get_monitoring_switches():
    networklist = monitoring.Monitoring(access_token, refresh_token, 'none')
    print(networklist.get_monitoring_v1_switches())

@cli.command()
def templatevars():
    print(json.dumps((template_vars.get_template_vars(access_token, templatevars))))

@cli.command()
def switchlist():
    print(json.dumps((switches.get_switches(access_token, refresh_token))))

@cli.command()
def networklist():
    print(json.dumps((networks.get_networks(access_token))))

@cli.command()
def grouplist():
    print(json.dumps((groups.get_groups(access_token))))

@cli.command()
@click.option('--groupname', help="Enter group name to search")
def group(groupname):
    #groupname = "Retail_AMER"
    print(json.dumps((groups.get_group(access_token, groupname))))

@cli.command()
def get_centraljson():
    print(centraljson.get_centraljson(access_token, refresh_token))

if __name__ == "__main__":
    cli()
