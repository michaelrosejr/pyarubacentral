#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, json, logging

class CentralAuth():
    def __init__(self, client_id, client_secret, envurl):
        self.client_id = client_id
        self.client_secret = client_secret
        self.envurl = envurl

        url = envurl + "/oauth2/token"


        payload = {'access_token': token}
        headers = {"Accept": "application/json"}

        response = requests.get(url, params=payload, headers=headers)
        if response.status_code != 200:
            #print(vars(get_access_token))
            print('Status:', get_access_token.status_code, 'Headers:', get_access_token.headers,
                  'Error Response:', get_access_token.reason)
            exit()

        self.response = response.json()

    def central_login(config):
        querystring = {"client_id": config["client_id"]}
        payload = "{\r\"username\": \"" + config['username'] + "\", \r\"password\": \"" + config['password'] + "\"\r}"

        # payload = {'username': 'michael@rozebud.com', 'password': 'Aruba123#'}
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache",
        }

        response = requests.post(config["url"] + "/oauth2/authorize/central/api/login", data=payload, headers=headers, params=querystring)
        logging.info(response.text)
        return (response.cookies)

    def get_auth_code_v2(cookies, config):

        querystring = {"client_id": config["client_id"], "response_type": "code", "scope": "all"}

        # payload = "{\n\"customer_id\": \"" + cookies['csrftoken'] + "\"\n}"
        payload = "{\n\"customer_id\": \"" + str(config['customer_id']) + "\"\n}"

        headers = {
            'content-type': "application/json",
            'x-csrf-token': cookies['csrftoken'],
            'cookie': "session=" + cookies['session'],
            'cache-control': "no-cache",
        }

        try:
            response = requests.post(config["auth_code_url"], data=payload, headers=headers, params=querystring)
            logging.info(response.text)
        except (requests.RequestException, requests.ConnectionError, requests.HTTPError) as error:
            print('\nRequests module exception: {}'.format(error.args))
        return (response.text)



    def refresh_token(self, client_id, client_secret, refresh_token, envurl):

        url = envurl + "/oauth2/token"
        payload = {'refresh_token': refresh_token, 'client_id': client_id, 'client_secret': client_secret,
                   'grant_type': 'refresh_token' }
        response = requests.post(url, params=payload)
        if response.status_code != 200:
            #print(vars(get_access_token))
            print('Status:', response.status_code, 'Headers:', response.headers,
                  'Error Response:', response.reason)
            exit()

        with open("token.json", "w") as exjsonfile:
            json.dump(response.json(), exjsonfile)

        print("RESPONSE: ", response.json())

    def get_login_cookies(config):
        querystring = {"client_id":config["client_id"]}
        payload = "{\r\"username\": \"" + config['username'] + "\", \r\"password\": \"" + config['password'] +"\"\r}"

        # payload = {'username': 'michael@rozebud.com', 'password': 'Aruba123#'}
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache",
            }


        response = requests.post(config["login_url"], data=payload, headers=headers, params=querystring)
        logging.info(response.text)
        return(response.cookies)


    def get_csrf_token(cookies, config, client_id):

        querystring = {"client_id": config["client_id"]}
        # payload = "{\r\"username\": \"" + config['username'] + "\", \r\"password\": \"" + config['password'] +"\"\r}"
        # payload = "{\n\"username\": \"" + str(username) + "\", \"password\": \"" + str(password) + "\"\n}"
        # payload = "{\n\"username\": \"" + config['username'] + "\", \"password\": \"" + config['password'] + "\"\n}"
        payload = {"username": config['username'], "password": config['password']}
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache",
            }

        response = requests.post(config["url"] + "/oauth2/authorize/central/api/login", data=json.dumps(payload), params=querystring, headers=headers)
        logging.info(response.text)
        return response.text

    def get_auth_code(cookies, config):


        querystring = {"client_id": config["client_id"],"response_type":"code","scope":"all"}

        # payload = "{\n\"customer_id\": \"" + cookies['csrftoken'] + "\"\n}"
        payload = "{\n\"customer_id\": \"" + str(config['customer_id']) + "\"\n}"

        headers = {
            'content-type': "application/json",
            'x-csrf-token': cookies['csrftoken'],
            'cookie': "session=" + cookies['session'],
            'cache-control': "no-cache",
            }

        response = requests.post(config["auth_code_url"], data=payload, headers=headers, params=querystring)
        logging.info(response.text)
        return(response.text)

    def get_access_tokens(config, auth_code):

        querystring = {"client_id": config['client_id'],"grant_type":"authorization_code","code": auth_code,"client_secret":config['client_secret']}

        headers = {
            'cache-control': "no-cache",
            }

        response = requests.post(config['url'] + "/oauth2/token", headers=headers, params=querystring)
        logging.info(response.text)
        return(response.text)

    def exchange_auth_code(self, client_id, client_secret, refresh_token, envurl):
        pass
