#!/usr/bin/env python3
import requests
import json
import click
import time, datetime
from collections import OrderedDict

from pyarubacentral import auth
import pyarubacentral.get_switches as switches
import pyarubacentral.get_groups as groups
import pyarubacentral.get_networks as networks
import pyarubacentral.get_template_vars as template_vars

with open('config.json', 'r') as f:
    config = json.load(f)

    client_id = config["client_id"]
    client_secret = config["client_secret"]
    tokenfile = config["tokenfile"]

with open(tokenfile) as exjsonfile:
    exchange_data = json.load(exjsonfile)



refresh_token = exchange_data["refresh_token"]
access_token = exchange_data["access_token"]
# created_at = exchange_data["created_at"]
expires_in = exchange_data["expires_in"]
expires_on = exchange_data["expires_on"]
# print("EX On: {}".format(format(datetime.datetime.fromtimestamp(int(expires_on)).strftime('%Y-%m-%d %H:%M:%S'))))

if time.time() > expires_on:
    print("Refresh me, for I have expired on {}".format(format(datetime.datetime.fromtimestamp(int(expires_on)).strftime('%Y-%m-%d %H:%M:%S'))))
    url = "https://app1-apigw.central.arubanetworks.com/oauth2/token"
    payload = {'refresh_token': refresh_token, 'client_id': client_id, 'client_secret': client_secret,
               'grant_type': 'refresh_token'}
    response = requests.post(url, params=payload)
    tokenconfig = response.json()
    tokenconfig['expires_on'] = time.time() + tokenconfig['expires_in']
    with open(tokenfile, "w") as exjsonfile:
        json.dump(tokenconfig, exjsonfile)


@click.command()
@click.option('--switchlist', flag_value=1)
@click.option('--grouplist', flag_value=1)
@click.option('--networklist', flag_value=1)
@click.option('--refresh', flag_value=1)
@click.option('--group', flag_value=1)
@click.option('--templatevars')
def app(switchlist, grouplist, networklist, refresh, group, templatevars):

    if refresh:
        url = "https://app1-apigw.central.arubanetworks.com/oauth2/token"
        payload = {'refresh_token': refresh_token, 'client_id': client_id, 'client_secret': client_secret, 'grant_type': 'refresh_token' }
        response = requests.post(url, params=payload)
        tokenconfig = response.json()
        tokenconfig['expires_on'] = time.time() + tokenconfig['expires_in']
        with open(tokenfile, "w") as exjsonfile:
            json.dump(response.json(), exjsonfile)


    if switchlist:
        print(json.dumps((switches.get_switches(access_token, refresh_token))))

    if grouplist:
        print(json.dumps((groups.get_groups(access_token))))

    if group:
        groupname = "Retail_AMER"
        print(json.dumps((groups.get_group(access_token, groupname))))

    if networklist:
        print(json.dumps((networks.get_networks(access_token))))

    if templatevars:
        print(json.dumps((template_vars.get_template_vars(access_token, templatevars))))


if __name__ == "__main__":
    app()
