#!/usr/bin/env python3
import requests
import json
import click
from collections import OrderedDict

from pyarubacentral import auth
import pyarubacentral.get_switches as switches
import pyarubacentral.get_groups as groups
import pyarubacentral.get_networks as networks


client_id = ""
client_secret = ""


@click.command()
@click.option('--switchlist', flag_value=1)
@click.option('--grouplist', flag_value=1)
@click.option('--networklist', flag_value=1)
def app(switchlist, grouplist, networklist):
    with open("token.json") as exjsonfile:
        exchange_data = json.load(exjsonfile)

    refresh_token = exchange_data["refresh_token"]
    access_token = exchange_data["access_token"]

    if switchlist:
        print(json.dumps((switches.get_switches(access_token))))

    if grouplist:
        print(json.dumps((groups.get_groups(access_token))))

    if networklist:
        print(json.dumps((networks.get_networks(access_token))))

    # if switchlist:
    #     switch_data = getSwitches(access_token)
    #     # pprint.pprint(switch_data)
    #     # print("Count: %s %s" %
    #     # [switch_data][0]["switches"][0]["firmware_version"])
    #
    #     # for switchdata in switch_data[0]:
    #     for listswitches in switch_data["switches"]:
    #         print('\n')
    #
    #         b = OrderedDict(sorted(listswitches.items()))
    #         for k, v in b.items():
    #             print(bcolors.OKBLUE + '{} : '.format(k) + bcolors.OKGREEN +
    #                   '{}'.format(v) + bcolors.RESET)




if __name__ == "__main__":
    app()
