#!/usr/bin/env python3

import argparse
import os, sys
import json
import logging

parser = argparse.ArgumentParser(description="Interact with Aruba Central")
parser.add_argument(
    "--refresh", dest="profile", help="Refresh access token for profile"
)
parser.add_argument(
    "--newtoken", dest="newtoken", help="Generate new access token for profile"
)
parser.add_argument(
    "--configure",
    action="store_true",
    help="Create configuration files for pyarubacentral module",
)
parser.add_argument(
    "-d",
    "--debug",
    help="Print lots of debugging statements",
    action="store_const",
    dest="loglevel",
    const=logging.DEBUG,
    default=logging.WARNING,
)
parser.add_argument(
    "-v",
    "--verbose",
    help="Be verbose",
    action="store_const",
    dest="loglevel",
    const=logging.INFO,
)

args = parser.parse_args()
logging.basicConfig(level=args.loglevel)

logger = logging.getLogger(__name__)
logger.setLevel(args.loglevel)
ch = logging.StreamHandler()
ch.setLevel(args.loglevel)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

# TODO: move location of configuration files to config.yml instead of hard coded
config_dir = os.environ["HOME"] + "/.arubacentral/"
yaml_files = ["accounts.yml", "regions.yml", "config.yml"]

import functools
class LogDecorator(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def __call__(self, fn):
        @functools.wraps(fn)
        def decorated(*args, **kwargs):
            try:
                self.logger.debug("{0} - {1} - {2}".format(fn.__name__, args, kwargs))
                result = fn(*args, **kwargs)
                self.logger.debug(result)
                return result
            except Exception as ex:
                self.logger.debug("Exception {0}".format(ex))
                raise ex
            return result
        return decorated

@LogDecorator()
def copy_config_files(backup):
    for conffile in yaml_files:
        print("Copying file " + conffile + " to " + config_dir + "....")
        if backup == 1:
            os.system(
                "mv " + config_dir + conffile + " " + config_dir + conffile + ".backup"
            )
        os.system(
            "wget -O "
            + config_dir
            + conffile
            + " https://raw.githubusercontent.com/michaelrosejr/pyarubacentral/master/samplescripts/"
            + conffile
            + ".sample"
        )
    print(
        "\nUse your favorite editor and edit the following files for your Aruba Central accounts:"
    )
    for editconf in yaml_files:
        print("\t" + config_dir + editconf)

@LogDecorator()
def check_config(args):
    if args.configure == True:
        print("Checking for existing configuration files....")
        if os.path.exists(config_dir) == False:
            print("Making directory " + config_dir)
            os.system("mkdir -p " + config_dir + "/tokens")
            fexist = False

        for chkfile in yaml_files:
            pwd = config_dir + chkfile
            if os.path.exists(pwd) == True:
                print("\tFile exists: " + pwd)
                fexist = True

            # print(os.path.exists('~/.arubacentral/accounts.yml'))
            # print(os.environ["HOME"])
        if fexist == True:
            print("\nDo you want to overwrite these files? [Y/N]: ", end="")
            yn = str(input())
            if yn.lower() == "y":
                copy_config_files(backup=1)
            else:
                print("Exiting...\n")
        else:
            copy_config_files(backup=0)
            print("\nExiting...")

@LogDecorator()
def authcode(profile):
    import pyarubacentral

    session = pyarubacentral.start_session(profile)
    logindata = session.get_authcode(session.get_login())
    access_token = json.loads(session.get_access_token(logindata))["access_token"]
    print("\nAccess Token: {}\n".format(access_token))

@LogDecorator()
def refresh(profile):
    import pyarubacentral

    session = pyarubacentral.start_session(profile)
    access_token = pyarubacentral.check_if_expired(profile, session)
    print("\n[{}]".format(profile))
    print("Access Token: " + access_token + "\n")

@LogDecorator()
def main():
    # print(args)
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    elif args.configure == True:
        check_config(args)
    elif args.profile:
        refresh(args.profile)
    elif args.newtoken:
        authcode(args.newtoken)


if __name__ == "__main__":
    main()
