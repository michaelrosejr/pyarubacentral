#!/usr/bin/env python3

import requests, json
from pyarubacentral import auth


def get_wifi_clients(sessiondata, group):
    url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/clients/wireless?group=" + group
    payload = {'access_token': sessiondata['access_token']}
    headers = {"Accept": "application/json"}

    response = requests.get(url, params=payload, headers=headers)

    return response.json()

def get_wifi_aps(sessiondata, group):
    url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/aps?group=" + group
    payload = {'access_token': sessiondata['access_token']}
    headers = {"Accept": "application/json"}

    response = requests.get(url, params=payload, headers=headers)

    return response.json()



def get_ble_addr(sessiondata):
    #
    #
    #
    url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/aps/detail"
    payload = {'access_token': sessiondata['access_token']}
    headers = {"Accept": "application/json"}

    response = requests.get(url, params=payload, headers=headers)

    return response.json()
