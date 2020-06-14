#!/usr/bin/env python3
import requests
import json
import yaml
import os
import logging
import time
import sys
import argparse 
from shutil import copyfile
from datetime import datetime, timedelta


# Enable logging. If its too verbose, change DEBUG to ERROR or another level
logging.basicConfig(level=logging.WARN)

# configpathfor Aruba Central config files
# default ~/.arubacentral/
configpath= os.environ.get('HOME') + "/.arubacentral"
# configpath= "./"


class Config:
    def __init__(self, profile):
        self.profile = profile

        
    def read_accounts(self, account):
        if os.path.isfile( configpath+ "/accounts.yml"):
            with open("/accounts.yml", 'r') as ymlfile:
                data = yaml.load(ymlfile, Loader=yaml.FullLoader)
            return data
        else: 
            print("Please read the README file and create the accounts.yml file using the sample.accounts.yml as a guide")
    
    def read_config(self):
        if os.path.isfile( configpath+ "/config.yml"):
            with open( configpath + "/config.yml", 'r') as ymlfile:
                cfgdata = yaml.load(ymlfile, Loader=yaml.FullLoader)
            
            # Get list of Centrla accounts
            if os.path.isfile( configpath+ "/accounts.yml"):
                with open( configpath + "/accounts.yml", 'r') as ymlfile:
                    accounts = yaml.load(ymlfile, Loader=yaml.FullLoader)
            else: 
               print("Please read the README file and create the accounts.yml file using the sample.accounts.yml as a guide")
     
            # Get Central regions
            if os.path.isfile( configpath+ "/regions.yml"):
                with open( configpath + "/regions.yml", 'r') as ymlfile:
                    regions = yaml.load(ymlfile, Loader=yaml.FullLoader)
            else: 
                print("Please read the README file and create the regions.yml file using the sample.regions.yml as a guide")

            data = {}
            try:
                data.update(cfgdata[self.profile])
            except Exception:
                logging.error('Profile not found. Please create a profile in ~/.arubacentra/accounts.yml')
                exit(0)
            data.update(accounts[cfgdata[self.profile]['user_account']])
            data.update( {"url": regions[cfgdata[self.profile]['region']]['url']} )
            data.update( {"profile": self.profile} )

            # print(data)
            
            return data
        else: 
            print("Please read the README file and create the config.yml file using the sample.config.yml as a guide")

class CentralAuth:
    def __init__(self, cfgdata):
        self.cfgdata = cfgdata
        self.profile = cfgdata['profile']
    
    def get_login(self):
        auth_url = self.cfgdata['url'] + "/oauth2/authorize/central/api/login"
        params = { "client_id": self.cfgdata['client_id'] }
        headers = { "Content-Type": "application/json" }
        data = { "username": self.cfgdata['username'], "password": self.cfgdata['password'] }
        s = requests.Session()
        r = s.post(auth_url, headers=headers, params=params, data=json.dumps(data), verify=True, timeout=10)
        if r.status_code == 200:
            for i in r.cookies:
                if i.name == "csrftoken":
                    csrftoken = i.value
                if i.name == "session":
                    csession = i.value
        else:
            print("ERROR CODE: " + str(r.status_code))
            print("ERORR Detail: " + str(r.text))
            print("\nERROR : The information in the config or accounts YAML files are incorrect.\nERROR : Please check your configuration and ARruba Central settings are corect\n")
        
        logincookies = {
            "csrftoken": csrftoken,
            "csession": csession
        }

        return logincookies

    def get_authcode(self, sdata):
        auth_url = self.cfgdata['url'] + "/oauth2/authorize/central/api"
        csrftoken = sdata['csrftoken']
        csession = sdata['csession']
        headers = {"Content-Type":"application/json",
                    "X-CSRF-TOKEN": csrftoken,
                    "Cookie":"session="+ csession}   
        params = {"client_id": self.cfgdata['client_id'], "response_type": "code", "scope": "all"}
        data = {"customer_id" : str(self.cfgdata['customer_id'])}
        s = requests.Session()
        result = s.post(auth_url, headers=headers, params=params,
                        data=json.dumps(data), verify=True, timeout=10)
        if result.status_code == 200 :
            tmp = json.loads(result.text)
            authcode = tmp['auth_code']
        else :
            print("status code : " + str(result.status_code))
            print("text : " + str(result.text))
            exit(0)

        logging.debug("authcode: %s", authcode)
        return authcode

    def get_access_token(self, authcode):
        token_url = self.cfgdata['url'] + "/oauth2/token"
        data = {}
        headers = {}
        params = {"client_id": self.cfgdata['client_id'], "client_secret": self.cfgdata['client_secret'], 
                    "grant_type": "authorization_code", "code": authcode}
        r = requests.post(token_url, headers=headers, params=params,
                        data=json.dumps(data), verify=True, timeout=10)
        if r.status_code == 200:
            tokens = json.loads(r.text)
            #
            # Set expire time less than 120 seconds for a buffer
            #
            expires_at_dt = datetime.now() + timedelta(0, (tokens['expires_in'] - 120))
            expires_at_epoc = expires_at_dt.timestamp()
            tokens.update({'expires_at':  expires_at_epoc })
            with open( configpath + "/tokens/" + self.profile + ".token.json", 'w') as newtokenfile:
                newtokenfile.write(json.dumps(tokens))

            return json.dumps(tokens)
        else:
            print("STATUS CODE: {} \nDetail: {}".format(str(r.status_code), str(r.text)))

    def refresh_access_token(self, tokens):
        token_url = self.cfgdata['url'] + "/oauth2/token"
        data = {}
        headers = {}
        params = {"client_id": self.cfgdata['client_id'], "client_secret": self.cfgdata['client_secret'], 
                    "grant_type": "refresh_token", "refresh_token": tokens['refresh_token']}
        r = requests.post(token_url, headers=headers, params=params,
                        data=json.dumps(data), verify=True, timeout=10)
        if r.status_code == 200:
            tokens = json.loads(r.text)
            #
            # Set expire time less than 120 seconds for a buffer
            #
            expires_at_dt = datetime.now() + timedelta(0, (tokens['expires_in'] - 120))
            expires_at_epoc = expires_at_dt.timestamp()
            tokens.update({'expires_at':  expires_at_epoc })
            with open( configpath + "/tokens/" + self.profile + ".token.json", 'w') as newtokenfile:
                newtokenfile.write(json.dumps(tokens))

            return json.dumps(tokens)
        else:
            print("STATUS CODE: {} \nDetail: {}".format(str(r.status_code), str(r.text)))

    def token_expired(self, access_token):
        expires_at = datetime.fromtimestamp(access_token['expires_at'])
        if datetime.now() > expires_at:
            logging.debug("Access token expired, refresh requested.")
            return 1
        else:
            logging.debug("Access token valid. Expires at: %s ", expires_at)
            return 0

        
    def get_user_account_list(self, access_token):
        token_url = self.cfgdata['url'] + "/platform/rbac/v1/users"
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
            }
        data = {
            'access_token': access_token
        }
        r = requests.get(token_url, headers=headers, data=json.dumps(data), verify=True, timeout=10)
        if r.status_code == 200:
            return r.text
        else:
            print("STATUS CODE: {} \nDetail: {}".format(str(r.status_code), str(r.text)))      

def configure():
    # Create directory to save configuration and token files
    try:
        os.makedirs(configpath+ "/tokens")
        print("Directory '{}' created".format(configpath+ "/tokens"))
    except Exception:
        print("Directory '{}' already created. ".format(configpath+ "/tokens"))

    # Copy Aruba Central API URLs files
    if not os.path.exists(configpath+ "/regions.yml"):
        copyfile("regions.yml", configpath + "/regions.yml")
        print("regions.yml file copied to `{}` directory. ".format(configpath+"/"))
    else:
        print("regions.yml already exists in `{}`. ".format(configpath + "/"))
       
    # Create config file for yaml
    print("The next portion of this configuration will require the following from Aruba Central:\n \
         If you do not have this informaiton, please login to Aruba Central API gateway and create\n\
             an API account.\
    \nclient_id\nclient_secret\ncustomer_id\nregion\n\
    ")
    doyouhavethisinfonow = input("Do you have the above information (Y/N): ")
    if doyouhavethisinfonow.lower() != "n":
        client_id = input("Client ID: ")
        client_secret = input("Client Securet: ")
        customer_id = input("Customer ID: ")
        profile_name = input("What is the profile name for this account: ")
        if profile_name.isspace():
            profile_name = input("The profile name cannot have a space in it. Please select a new profile name\n")
        with open ( configpath + "/regions.yml") as reg:
            regions = yaml.load(reg, Loader=yaml.FullLoader)
        print("\n")
        for j in regions.items():
            print(j)
        region = input("\nWhich region are you using. [US-2] : ")

        check = 0
        while (check < 1):
            if region == "":
                region = "US-2"
            else:
                if region in regions.keys():
                    print("Setting region to " + region)
                    check = 2
                else: 
                    print("region not found. ")
                    region = input("Which region are you using. [US-2] : ")
                    check = 0
        
        print("\nPlease confirm your settings:\n\nclient_id= {}\nclient_secret= {}\ncustomer_id= {}\nprofile_name= {}\nregion= {}\n".format(profile_name, client_id, client_secret, customer_id, region))
        confirm_settings = input("Are these settings correct [Y/N]: ")

        newconfigyaml = {
            profile_name: {
                "client_id": client_id,
                "client_secret": client_secret,
                "customer_id": customer_id,
                "region": region,
                "user_account": "FIXME"
            }    
        }
        if confirm_settings.lower() == "y":
            with open(configpath + "/config.yml", "a") as cnfile:
                yaml.dump(newconfigyaml, cnfile)
                print("Writing configuration file to `{}` . ".format(configpath + "/config.yml"))
                print("If you need to make changes, please edit this file with your favorite YAML editor")


def check_if_expired(profile, session):
    with open( configpath + "/tokens/" + profile + ".token.json", 'r') as fp:
        access_token = json.load(fp) 

    if session.token_expired(access_token):
        # Get the access token, check if its has expired and if so, refresh the tokens.
        logging.debug(session.refresh_access_token(access_token))
        access_token = session.refresh_access_token(access_token)['access_token']
    return access_token['access_token']

def expires(profile):
    with open( configpath + "/tokens/" + profile + ".token.json", 'r') as fp:
        access_token = json.load(fp) 

    return datetime.fromtimestamp(access_token['expires_at'])

def start_session(profile):
    # Set the configuration from the configpathconfig files
    config = Config(profile).read_config()

    # create the session to store the config and tokens
    createsession = CentralAuth(config)
    return(createsession)

def main():
    tool_description = "This tool is used for creating and refreshing tokens for Aruba Central. This module can be imported as a python module for your own python scripts.\n To add additonal accounts, regions, configurations; please edit the files located in ~/.arubacentral/\n All tokens are stored in ~/.arubacentral/tokens"
    parser = argparse.ArgumentParser(description=tool_description, add_help=True)
    parser.add_argument("-p", "--profile", help = "Account Profile. Use this option to REFRESH new access_token")

    parser.add_argument("--configure", help = "Run the configuration tool to setup a new envrionment",
        action="store_true")
    parser.add_argument("--authcode", help = "Generate new authcode for expired refresh tokens. Use this if its been serveral \
        days since you've ran this script.", action="store_true")
    parser.add_argument("--centralusers", help = "List of users in Central account", action="store_true")
    parser.add_argument("--expires", help = "Show when token will expire", action="store_true")
    args = parser.parse_args()
    
    if args.configure:
        configure()
        exit(0)
    elif args.authcode:
        ## Get New Token
        session = start_session(args.profile)
        logindata = session.get_authcode(session.get_login())
        access_token = json.loads(session.get_access_token(logindata))['access_token']
        logging.debug("CentralAuth: %s", logindata)
        logging.debug("CentralAccessToken: %s", access_token)
        print("\nAccess Token: {}\n".format(access_token))


    ## Print user for account
    elif args.centralusers:
        session = start_session(args.profile)
        access_token = check_if_expired(args.profile, session)
        print(session.get_user_account_list(access_token))
    elif args.profile and args.expires:
        session = start_session(args.profile)
        access_token = check_if_expired(args.profile, session)
        print(expires(args.profile))

    elif args.profile:
        session = start_session(args.profile)
        access_token = check_if_expired(args.profile, session)
        print("\nAccess Token: {}\n".format(access_token))

    else:
        print("Missing commandline arguments. Use -h for help.")
        print("You may need to edit the files in ~/.arubacentral/ as well")
        print("See https://github.com/michaelrosejr.com/pyarubacentral for more detail")

if __name__ == "__main__":
    logging.info("Executing main...")
    main()