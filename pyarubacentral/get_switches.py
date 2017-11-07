#!/usr/bin/env python3

import requests, json
from pyarubacentral import auth


def get_switches(access_token, refresh_token):
    url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/switches"
    payload = {'access_token': access_token}
    headers = {"Accept": "application/json"}

    response = requests.get(url, params=payload, headers=headers)

    return response.json()
