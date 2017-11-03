#!/usr/bin/env python3

import requests, json
from pyarubacentral import auth

def get_groups(access_token):
    url = "https://app1-apigw.central.arubanetworks.com/configuration/v1/groups?limit=20&offset=1"
    payload = {'access_token': access_token}
    headers = {"Accept": "application/json"}

    response = requests.get(url, params=payload, headers=headers)

    return response.json()

def get_group(access_token, group_name):
    url = "https://app1-apigw.central.arubanetworks.com/configuration/v1/groups/"
    url = url + group_name
    payload = {'access_token': access_token}
    headers = {"Accept": "application/json"}

    response = requests.get(url, params=payload, headers=headers)

    return response.json()