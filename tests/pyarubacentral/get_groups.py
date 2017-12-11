#!/usr/bin/env python3

import requests, json
from pyarubacentral import auth

def get_groups(sessiondata):
    url = "https://app1-apigw.central.arubanetworks.com/configuration/v1/groups?limit=20&offset=1"
    payload = {'access_token': sessiondata['access_token']}
    headers = {"Accept": "application/json"}

    response = requests.get(url, params=payload, headers=headers)

    return response.json()

def get_group(sessiondata):
    url = "https://app1-apigw.central.arubanetworks.com/configuration/v1/groups/"
    url = url + group_name
    payload = {'access_token': sessiondata['access_token']}
    headers = {"Accept": "application/json"}

    response = requests.get(url, params=payload, headers=headers)

    return response.json()
