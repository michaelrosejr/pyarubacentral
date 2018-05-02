#!/usr/bin/env python3

import requests, json
from pyarubacentral import auth


def get_switches(sessiondata):
    url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/switches"
    payload = {'access_token': sessiondata['access_token']}
    headers = {"Accept": "application/json"}

    response = requests.get(url, params=payload, headers=headers)

    return response.json()

def get_switch_detials(sessiondata, serial):
    url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/switches/" + serial
    payload = {'access_token': sessiondata['access_token']}
    headers = {"Accept": "application/json"}

    response = requests.get(url, params=payload, headers=headers)

    return response.json()
