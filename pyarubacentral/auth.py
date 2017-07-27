#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, json

class CentralAuth():
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

        url = "https://app1-apigw.central.arubanetworks.com/oauth2/token"

        payload = {'access_token': token}
        headers = {"Accept": "application/json"}

        response = requests.get(url, params=payload, headers=headers)
        if response.status_code != 200:
            #print(vars(get_access_token))
            print('Status:', get_access_token.status_code, 'Headers:', get_access_token.headers,
                  'Error Response:', get_access_token.reason)
            exit()

        self.response = response.json()


