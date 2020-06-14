import requests

def get_central(sessiondata, url):
    """
    Login and get Aruba Central data
    """
    payload = {'access_token': sessiondata['access_token']}
    headers = {"Accept": "application/json"}

    try:
        r = requests.get(url, params=payload, headers=headers)
        if r.status_code != 200:
            print('Status:', r.status_code, 'Headers:', r.headers,
                  'Error Response:', r.reason)
        return r.text
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + sys._getframe().f_code.co_name + ": An Error has occured"


class Usermgmt():
    """ Central Usermgmt APIs """
    def __init__(self, sessiondata, pvalue):
        self.sessiondata = sessiondata


    def get_accounts_v2_users(self):
        """
        List user accoun
            Returns all users from the system associated to user's accou
        """
        url = self.sessiondata['baseurl'] + "/accounts/v2/users"
        response = get_central(self.sessiondata, url)
        return response


    def get_accounts_v1_roles(self):
        """
        Get all user rol
            None
        """
        url = self.sessiondata['baseurl'] + "/accounts/v1/roles"
        response = get_central(self.sessiondata, url)
        return response


    def get_accounts_v1_users_change_password(self):
        """
        Get all user rol
            None
        """
        url = self.sessiondata['baseurl'] + "/accounts/v1/users/change_password"
        response = get_central(self.sessiondata, url)
        return response


    def get_accounts_v1_users(self):
        """
        (Deprecated) List user accoun
            (Deprecated, Alternate API:/accounts/v2/users) Get User account detai
        """
        url = self.sessiondata['baseurl'] + "/accounts/v1/users"
        response = get_central(self.sessiondata, url)
        return response


    def get_accounts_v2_users_user_id(self):
        """
        Get User account detai
            None
        """
        url = self.sessiondata['baseurl'] + "/accounts/v2/users/" + self.pvalue
        response = get_central(self.sessiondata, url)
        return response


    def get_accounts_v1_users_user_id(self):
        """
        (Deprecated) Get User account detai
            (Deprecated, Alternate API:/accounts/v2/users/{user_id}) Get User account detai
        """
        url = self.sessiondata['baseurl'] + "/accounts/v1/users/" + self.pvalue
        response = get_central(self.sessiondata, url)
        return response


    def get_accounts_v1_roles_rolename(self):
        """
        Get User Role detai
            Get User Role detai
        """
        url = self.sessiondata['baseurl'] + "/accounts/v1/roles/" + self.pvalue
        response = get_central(self.sessiondata, url)
        return response
