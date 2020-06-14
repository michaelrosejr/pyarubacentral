#!/usr/bin/env python3

import argparse
import os, sys
import json

parser = argparse.ArgumentParser(description='Interact with Aruba Central')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
# parser.add_argument('--test', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')
parser.add_argument('--refresh', dest='profile',
                    help='Refresh access token for profile')
parser.add_argument('--newtoken', dest='newtoken',
                    help='Generate new access token for profile')
parser.add_argument('--configure', action="store_true",
                    help='Create configuration files for pyarubacentral module')

args = parser.parse_args()
# print(args.configure)

config_dir = os.environ["HOME"] + "/.arubacentral/"
yaml_files = ['accounts.yml', 'regions.yml', 'config.yml']

def copy_config_files(backup):
    for conffile in yaml_files:
        print("Copying file " + conffile + " to " + config_dir + "....")
        if backup == 1:
            os.system('mv ' + config_dir+conffile + ' ' + config_dir+conffile + '.backup')
        os.system('wget -O ' + config_dir+conffile + ' https://raw.githubusercontent.com/michaelrosejr/pyarubacentral/master/samplescripts/' + conffile + ".sample" )
    print("\nUse your favorite editor and edit the following files for your Aruba Central accounts:")
    for editconf in yaml_files:
        print("\t" + config_dir+editconf )

def check_config(args):
    if args.configure == True:
        print("Checking for existing configuration files....")
        if os.path.exists(config_dir) == False:
            print("Making directory " + config_dir)
            os.system('mkdir -p ' + config_dir + "/tokens")
            fexist = False
        
        for chkfile in yaml_files:
            pwd = config_dir+chkfile
            if os.path.exists(pwd) == True:
                print("\tFile exists: "+pwd)
                fexist = True
                  
            # print(os.path.exists('~/.arubacentral/accounts.yml'))
            # print(os.environ["HOME"])
        if fexist == True:
            print("\nDo you want to overwrite these files? [Y/N]: ", end = '')
            yn = str(input())
            if yn.lower() == "y":
                copy_config_files(backup=1)
            else: 
                print("Exiting...\n")    
        else:
            copy_config_files(backup=0)
            print("\nExiting...")

def authcode(profile):
    import pyarubacentral
    session = pyarubacentral.start_session(profile)
    logindata = session.get_authcode(session.get_login())
    access_token = json.loads(session.get_access_token(logindata))['access_token']
    print("\nAccess Token: {}\n".format(access_token))

def refresh(profile):
    import pyarubacentral
    session = pyarubacentral.start_session(profile)
    access_token = pyarubacentral.check_if_expired(profile, session)
    print("\n[{}]".format(profile))
    print("Access Token: "+access_token+ "\n")

def main():
    # print(args)
    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    elif args.configure == True:
        check_config(args)
    elif args.profile:
        refresh(args.profile)
    elif args.newtoken:
        authcode(args.newtoken)


if __name__== "__main__":
   main()