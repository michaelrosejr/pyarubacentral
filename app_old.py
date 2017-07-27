#!/usr/bin/env python3
import requests
import pprint
import json
import click
from collections import OrderedDict

#
# Central API Gateway
# app1-apigw.central.arubanetworks.com
#


class bcolors:
    """Colors used for console output."""

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\x1b[0m'


@click.command()
@click.option('--exchange', flag_value=1)
@click.option('--switchlist', flag_value=1)
@click.option('--refresh', flag_value=1)
@click.option('--grouplist', flag_value=1)
@click.option('--templatevars')
@click.option('--networklist', flag_value=1)
def cli(exchange, switchlist, refresh, grouplist, templatevars, networklist):
    """ Execute CLI command to query Central API."""
    with open("token.json") as exjsonfile:
        exchange_data = json.load(exjsonfile)

    refresh_token = exchange_data["refresh_token"]
    access_token = exchange_data["access_token"]



    if exchange:
        TokenUpdate('exchange', 'none')

    if refresh:
        TokenUpdate('refresh', refresh_token)

    if switchlist:
        switch_data = getSwitches(access_token)
        # pprint.pprint(switch_data)
        # print("Count: %s %s" %
        # [switch_data][0]["switches"][0]["firmware_version"])

        # for switchdata in switch_data[0]:
        for listswitches in switch_data["switches"]:
            print('\n')

            b = OrderedDict(sorted(listswitches.items()))
            for k, v in b.items():
                print(bcolors.OKBLUE + '{} : '.format(k) + bcolors.OKGREEN +
                      '{}'.format(v) + bcolors.RESET)

            # print("Count: %s" % listswitches)

    if grouplist:
        group_data = getGroups(access_token)
        pprint.pprint(group_data)

    if networklist:
        network_data = getNetworks(access_token)
        pprint.pprint(network_data)


def TokenUpdate(uptype, refresh_token):
    """Refresh, Exchange Token from Central."""
    url = "https://app1-apigw.central.arubanetworks.com/oauth2/token"
    client_id = "aa5eb84c499e4964beb41766ff4975e2"
    client_secret = "b6bf3aa2d482455ba3e289b6f1d5ad6f"
    auth_code = ""

    if uptype == "refresh":
        filename = "token.json"
        grant_type = "refresh_token"
        payload = {'client_id': client_id, 'grant_type': "refresh_token",
                   'refresh_token': refresh_token,
                   'client_secret': client_secret}
    elif uptype == "exchange":
        filename = "token.json"
        grant_type = "authorization_code"
        payload = {'client_id': client_id, 'grant_type': "authorization_code",
                   'code' : auth_code, 'client_secret': client_secret}
    else:
        filename = "else.json"
        grant_type = "code"

    headers = {"Accept": "application/json"}

    # Do the HTTP request
    response = requests.post(url, params=payload, headers=headers)
    #click.echo("URL: " + response.url)
    if response.status_code != 200:
        print('Status:', response.status_code, 'Headers:', response.headers,
              'Error Response:', response.json())
        exit()

    json_data = response.json()

    if 'uptype' in locals():
        with open(filename, "w") as f:
            json.dump(json_data, f)

    pprint.pprint(json_data)


def getNetworks(access_token):
    url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/networks"
    return APIQuery(url, access_token)


def getSwitches(access_token):
    url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/switches"
    return APIQuery(url, access_token)


def getGroups(access_token):
    url = "https://app1-apigw.central.arubanetworks.com/configuration/v1/"
    "groups?limit=20&offset=1"
    return APIQuery(url, access_token)


def APIQuery(url, access_token):
    payload = {'access_token': access_token}
    headers = {"Accept": "application/json"}

    response = requests.get(url, params=payload, headers=headers)
    #click.echo("URL: " + response.url)
    # Check for HTTP codes other than 200
    if response.status_code != 200:
        print('Status:', response.status_code, 'Headers:', response.headers,
              'Error Response:', response.json())

        CentralError = response.json()
        #pprint.pprint(CentralError)
        #print(("Error: %s") % ([CentralError][0]['error']))
        if [CentralError][0]['error'] == "invalid_token":
            print(bcolors.OKBLUE + "Refreshing token..." + bcolors.RESET)
            with open("token.json") as exjsonfile:
                exchange_data = json.load(exjsonfile)

            refresh_token = exchange_data["refresh_token"]
            access_token = exchange_data["access_token"]
            TokenUpdate('refresh', refresh_token)
            print(bcolors.OKBLUE + "Token refreshed. Please execute command again" + bcolors.RESET)

        exit()

    return response.json()




if __name__ == "__main__":
    cli()
