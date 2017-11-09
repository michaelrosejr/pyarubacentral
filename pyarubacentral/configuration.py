#!/usr/bin/env python3

import requests
import json

def get_central(access_token, refresh_token, url):
    """
    Login and get Aruba Central data
    """
    payload = {'access_token': access_token}
    headers = {"Accept": "application/json"}

    try:
        r = requests.get(url, params=payload, headers=headers)
        if r.status_code != 200:
            print('Status:', r.status_code, 'Headers:', r.headers,
                  'Error Response:', r.reason)
        return r.text
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + sys._getframe().f_code.co_name + ": An Error has occured"

def push_central(access_token, refresh_token, url, data):
    """
    Login and push data to Aruba Central
    """
    payload = {'access_token': access_token}
    headers = {"Accept": "application/json"}

    try:
        r = requests.get(url, params=payload, headers=headers, data=data)
        if r.status_code != 200:
            print('Status:', r.status_code, 'Headers:', r.headers,
                  'Error Response:', r.reason)
        return r.text
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + sys._getframe().f_code.co_name + ": An Error has occured"

class Configuration():
    """ Central Monitoring APIs """
    def __init__(self, access_token, refresh_token, pvalue, data):
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.pvalue = pvalue
        self.data = data


    def get_configuration_v1_devices_template_variables(self):
        """
        Get template variables for all devices, Response is sorted by device_seri
            None
        """
        url = "https://app1-apigw.central.arubanetworks.com/configuration/v1/devices/" + self.pvalue + "/template_variables"
        response = push_central(self.access_token, self.refresh_token, url, self.data)
        return response


    def get_configuration_v1_devices_device_serial_recover_device(self):
        """
        Get template variables for all devices, Response is sorted by device_seri
            None
        """
        url = "https://app1-apigw.central.arubanetworks.com/configuration/v1/devices/" + self.pvalue + "/recover_device"
        response = push_central(self.access_token, self.refresh_token, url)
        return response


    def get_configuration_v1_certificates(self):
        """
        Get Certificates details upload
            None
        """
        url = "https://app1-apigw.central.arubanetworks.com/configuration/v1/certificates"
        response = push_central(self.access_token, self.refresh_token, url)
        return response


    def get_configuration_v1_mode_device(self):
        """
        Get config mode as either Monitor or Managed mode at device lev
            Get config mode as either Monitor or Managed mode at device level in given gro
        """
        url = "https://app1-apigw.central.arubanetworks.com/configuration/v1/mode/device"
        response = push_central(self.access_token, self.refresh_token, url)
        return response


    def get_configuration_v1_devices_device_serial_template_variables(self):
        """
        Get template variables for a devi
            None
        """
        url = "https://app1-apigw.central.arubanetworks.com/configuration/v1/devices/" + self.pvalue + "/template_variables"
        response = push_central(self.access_token, self.refresh_token, url)
        return response


    def get_configuration_v1_msp_templates_differences_device_type_version_model(self):
        """
        Get customers & groups where given MSP level template is not applie
            Get customers & groups where given MSP level template is not applie
        """
        url = "https://app1-apigw.central.arubanetworks.com/configuration/v1/msp/templates/differences/" + self.pvalue + "/" + self.pvalue + "/" + pvalue
        response = push_central(self.access_token, self.refresh_token, url)
        return response


    def get_configuration_v1_mode_group(self):
        """
        Get config mode for devices as either Monitor or Managed mode at group lev
            Get config mode as either Monitor or Managed mode at group lev
        """
        url = "https://app1-apigw.central.arubanetworks.com/configuration/v1/mode/group"
        response = push_central(self.access_token, self.refresh_token, url)
        return response


    def get_configuration_v1_groups_group_templates(self):
        """
        Get all templates in gro
            Get all templates in group. Query can be filtered by name, device_type, version, model or J number(for ArubaSwitch). Response is sorted by template na
        """
        url = "https://app1-apigw.central.arubanetworks.com/configuration/v1/groups/" + self.pvalue + "/templates"
        response = push_central(self.access_token, self.refresh_token, url)
        return response


    def get_configuration_v1_groups_default_group(self):
        """
        Get default gro
            Get default gro
        """
        url = "https://app1-apigw.central.arubanetworks.com/configuration/v1/groups/default_group"
        response = push_central(self.access_token, self.refresh_token, url)
        return response


    def get_configuration_v1_msp_templates_device_type_version_model(self):
        """
        Get MSP customer level template te
            Get MSP level template te
        """
        url = "https://app1-apigw.central.arubanetworks.com/configuration/v1/msp/templates/" + self.pvalue + "/" + self.pvalue + "/" + pvalue
        response = push_central(self.access_token, self.refresh_token, url)
        return response


    def get_configuration_v1_groups_group_templates_template(self):
        """
        Get template text for a template in gro
            Get template text for a template in grou
        """
        url = "https://app1-apigw.central.arubanetworks.com/configuration/v1/groups/" + self.pvalue + "/templates/" + pvalue
        response = push_central(self.access_token, self.refresh_token, url)
        return response


    def get_configuration_v1_devices_device_serial_variablised_template(self):
        """
        Get variabilised template for a devi
             Response information
			- -----BEGIN TEMPLATE-----
			-  template body
			-  -----END TEMPLATE-----

			-  -----BEGIN VARIABLES-----
			-  variables information
			-  -----END VARIABLES---
        """
        url = "https://app1-apigw.central.arubanetworks.com/configuration/v1/devices/" + self.pvalue + "/variablised_template"
        response = push_central(self.access_token, self.refresh_token, url)
        return response


    def get_configuration_v1_devices_move(self):
        """
        Get variabilised template for a devi
             Response information
			- -----BEGIN TEMPLATE-----
			-  template body
			-  -----END TEMPLATE-----

			-  -----BEGIN VARIABLES-----
			-  variables information
			-  -----END VARIABLES---
        """
        url = "https://app1-apigw.central.arubanetworks.com/configuration/v1/devices/move"
        response = push_central(self.access_token, self.refresh_token, url)
        return response


    def get_configuration_v1_groups(self):
        """
        Get all grou
            Get all groups, Response is sorted by group na
        """
        url = "https://app1-apigw.central.arubanetworks.com/configuration/v1/groups"
        response = push_central(self.access_token, self.refresh_token, url)
        return response


    def get_configuration_v1_mode(self):
        """
        Get config mode as either Monitor or Managed mode at customer lev
            Get config mode as either Monitor or Managed mode at customer lev
        """
        url = "https://app1-apigw.central.arubanetworks.com/configuration/v1/mode"
        response = push_central(self.access_token, self.refresh_token, url)
        return response


    def get_configuration_v1_groups_group(self):
        """
        Get gro
            Get gro
        """
        url = "https://app1-apigw.central.arubanetworks.com/configuration/v1/groups/" + pvalue
        response = push_central(self.access_token, self.refresh_token, url)
        return response


    def get_configuration_v1_devices_device_serial_clis(self):
        """
        Get gro
            Get gro
        """
        url = "https://app1-apigw.central.arubanetworks.com/configuration/v1/devices/" + self.pvalue + "/clis"
        response = push_central(self.access_token, self.refresh_token, url)
        return response


    def get_configuration_v1_certificates_certificate(self):
        """
        Get gro
            Get gro
        """
        url = "https://app1-apigw.central.arubanetworks.com/configuration/v1/certificates/" + pvalue
        response = push_central(self.access_token, self.refresh_token, url)
        return response


    def get_configuration_v1_devices_device_serial_config_details(self):
        """
        Get configuration details for a device(only for template group
            Get central side configuration, device running configuration, configuration error details, template error details and status of a device belonging to a template grou
        """
        url = "https://app1-apigw.central.arubanetworks.com/configuration/v1/devices/" + self.pvalue + "/config_details"
        response = push_central(self.access_token, self.refresh_token, url)
        return response


    def get_configuration_v1_cplogo(self):
        """
        Get Captive Portal Logos upload
            None
        """
        url = "https://app1-apigw.central.arubanetworks.com/configuration/v1/cplogo"
        response = push_central(self.access_token, self.refresh_token, url)
        return response


    def get_configuration_v1_devices_device_serial_ssh_connection(self):
        """
        Get Captive Portal Logos upload
            None
        """
        url = "https://app1-apigw.central.arubanetworks.com/configuration/v1/devices/" + self.pvalue + "/ssh_connection"
        response = push_central(self.access_token, self.refresh_token, url)
        return response


    def get_configuration_v1_devices_device_serial_group(self):
        """
        Get group for a devi
            None
        """
        url = "https://app1-apigw.central.arubanetworks.com/configuration/v1/devices/" + self.pvalue + "/group"
        response = push_central(self.access_token, self.refresh_token, url)
        return response


    def get_configuration_v1_msp_templates_differences_customer_cid_device_type_version_model(self):
        """
        Get groups where given END customer level template is not applie
            Get groups where given END customer level template is not applie
        """
        url = "https://app1-apigw.central.arubanetworks.com/configuration/v1/msp/templates/differences/customer/" + self.pvalue + "/" + self.pvalue + "/" + self.pvalue + "/" + pvalue
        response = push_central(self.access_token, self.refresh_token, url)
        return response


    def get_configuration_v1_devices_device_serial_assign_mm_mm_name(self):
        """
        Get groups where given END customer level template is not applie
            Get groups where given END customer level template is not applie
        """
        url = "https://app1-apigw.central.arubanetworks.com/configuration/v1/devices/" + self.pvalue + "/assign_mm/" + pvalue
        response = push_central(self.access_token, self.refresh_token, url)
        return response


    def get_configuration_v1_msp_templates(self):
        """
        Get MSP customer level template detai
            Get all MSP customer level templates details. Query can be filtered by device_type, version, mode
        """
        url = "https://app1-apigw.central.arubanetworks.com/configuration/v1/msp/templates"
        response = push_central(self.access_token, self.refresh_token, url)
        return response


    def get_configuration_v1_devices_device_serial_configuration(self):
        """
        Get last known running configuration for a devi
            None
        """
        url = "https://app1-apigw.central.arubanetworks.com/configuration/v1/devices/" + self.pvalue + "/configuration"
        response = push_central(self.access_token, self.refresh_token, url)
        return response


    def get_configuration_v1_groups_group_clis_(self):
        """
        Get last known running configuration for a devi
            None
        """
        url = "https://app1-apigw.central.arubanetworks.com/configuration/v1/groups/" + self.pvalue + "/clis/"
        response = push_central(self.access_token, self.refresh_token, url)
        return response


    def get_configuration_v1_msp_templates_customer_cid_device_type_version_model(self):
        """
        Get END customer level template te
            Get MSP level template te
        """
        url = "https://app1-apigw.central.arubanetworks.com/configuration/v1/msp/templates/customer/" + self.pvalue + "/" + self.pvalue + "/" + self.pvalue + "/" + pvalue
        response = push_central(self.access_token, self.refresh_token, url)
        return response


    def get_configuration_v1_cplogo_checksum(self):
        """
        Get END customer level template te
            Get MSP level template te
        """
        url = "https://app1-apigw.central.arubanetworks.com/configuration/v1/cplogo/" + pvalue
        response = push_central(self.access_token, self.refresh_token, url)
        return response


    def get_configuration_v1_msp_templates_customer_cid(self):
        """
        Get END customer level template detai
            Get all END customer level templates details. Query can be filtered by device_type, version, mode
        """
        url = "https://app1-apigw.central.arubanetworks.com/configuration/v1/msp/templates/customer/" + pvalue
        response = push_central(self.access_token, self.refresh_token, url)
        return response
