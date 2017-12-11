#!/usr/bin/env python3

import requests, json
from pyarubacentral import auth

def get_networks(sessiondata):
    url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/networks"
    payload = {'access_token': sessiondata['access_token']}
    headers = {"Accept": "application/json"}

    response = requests.get(url, params=payload, headers=headers)

    return response.json()
