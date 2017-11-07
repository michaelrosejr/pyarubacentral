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


class monitoring():
    """ Central Monitoring APIs """


    def get_monitoring_v1_swarms_swarm_id(access_token, refresh_token):
        """
        Swarm Detai
        Get Swarm detail
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/swarms/{swarm_id}"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_clients_wireless_macaddr(access_token, refresh_token):
        """
        Wireless Client Detai
        Get wireless client detail
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/clients/wireless/{macaddr}"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_mobility_controllers_serial_tunnels(access_token, refresh_token):
        """
        Mobility Controllers Uplink Tunnel Detai
        Get mobility controller's Uplink tunnel details.
        Possible error_codes for the error responses are
        1. 0001 - General Error
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/mobility_controllers/{serial}/tunnels"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v2_aps_serial_rf_summary(access_token, refresh_token):
        """
        AP RF Summa
        Get AP RF summary of channel utilization, noise floor in negative, errors, drops and retries over a time period.
        Possible error_codes for the error responses are
        1. 0001 - General Error.
        2. 0002 - Validation Error. Out of Range value for a query parameter.
        3. 0004 - Validation Error. Invalid value for a query paramete
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v2/aps/{serial}/rf_summary"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_mobility_controllers_uplinks_bandwidth_usage(access_token, refresh_token):
        """
        Uplink Bandwidth Usa
        Get uplink bandwidth usage over a time period. You can only specify one of group, label, serial parameters.
        Possible error_codes for the error responses are
        1. 0001 - General Error.
        2. 0002 - Validation Error. Out of Range value for a query parameter.
        3. 0003 - Validation Error. Unsupported query combination
        4. 0004 - Validation Error. Invalid value for a query parameter
        5. 0005 - Validation Error. Missing required parameter
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/mobility_controllers/uplinks/bandwidth_usage"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_wids_client_attacks(access_token, refresh_token):
        """
        List Client Attac
        Get client attacks over a time perio
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/wids/client_attacks"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_mobility_controllers_serial(access_token, refresh_token):
        """
        Mobility Controller Detai
        Get mobility controller detail
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/mobility_controllers/{serial}"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_networks(access_token, refresh_token):
        """
        List all Networ
        Get a list of networks. You can only specify one of group, swarm_id, label parameters.
        Possible error_codes for the error responses are
        1. 0001 - General Error.
        2. 0003 - Validation Error. Unsupported query combination
        3. 0004 - Validation Error. Invalid value for a query paramete
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/networks"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_clients_wired(access_token, refresh_token):
        """
        List Wired Clien
        Get a list of wired clients. You can only specify one of group, swarm_id, cluster_id, stack_id and
        label parameters.
        Possible error_codes for the error responses are
        1. 0001 - General Error.
        2. 0002 - Validation Error. Out of Range value for a query parameter.
        3. 0003 - Validation Error. Unsupported query combination
        4. 0004 - Validation Error. Invalid value for a query paramete
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/clients/wired"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_networks_bandwidth_usage(access_token, refresh_token):
        """
        WLAN Network Bandwidth usa
        Get WLAN network bandwidth usage over a time period. You can only specify one of group, swarm_id, label parameters.
        Possible error_codes for the error responses are
        1. 0001 - General Error.
        2. 0002 - Validation Error. Out of Range value for a query parameter.
        3. 0003 - Validation Error. Unsupported query combination
        4. 0005 - Validation Error. Missing required parameter
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/networks/bandwidth_usage"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_switch_stacks(access_token, refresh_token):
        """
        Switch Stack Detai
        List Switch Stack
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/switch_stacks"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_attribute_values(access_token, refresh_token):
        """
        List Attribute Valu
        Get list of attribute values
        Possible error_codes for the error responses are
        1. 0001 - General Error.
        2. 0004 - Validation Error. Invalid value for a query paramete
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/attribute_values"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_vpn_usage(access_token, refresh_token):
        """
        Swarm VPN sta
        Get VPN usages per tunnel (primary/backup) over a time period.
        Possible error_codes for the error responses are
        1. 0001 - General Error.
        2. 0002 - Validation Error. Out of Range value for a query parameter.
        3. 0004 - Validation Error. Invalid value for a query paramete
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/vpn/usage"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_aps_serial(access_token, refresh_token):
        """
        AP Detai
        Get AP detail
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/aps/{serial}"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_central_v1_labels_label_id(access_token, refresh_token):
        """
        Label detai
        Get a label detail
        """
        url = "https://app1-apigw.central.arubanetworks.com/central/v1/labels/{label_id}"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_mobility_controllers_uplinks_wan_compression_stats(access_token, refresh_token):
        """
        Uplink WAN compression sta
        Get WAN compression stats over a time period. You can only specify one of group, label, serial parameters.
        Possible error_codes for the error responses are
        1. 0001 - General Error.
        2. 0002 - Validation Error. Out of Range value for a query parameter.
        3. 0003 - Validation Error. Unsupported query combination
        4. 0004 - Validation Error. Invalid value for a query parameter
        5. 0005 - Validation Error. Missing required parameter
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/mobility_controllers/uplinks/wan_compression_stats"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_switch_stacks_stack_id(access_token, refresh_token):
        """
        Switch Stack Detai
        Get Switch Stack detail
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/switch_stacks/{stack_id}"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_aps_bandwidth_usage_topn(access_token, refresh_token):
        """
        Top N AP Detai
        Get top N AP details over a time period. You can only specify one of group, swarm_id, label, cluster_id
        parameters.
        Possible error_codes for the error responses are
        1. 0001 - General Error.
        2. 0002 - Validation Error. Out of Range value for a query parameter.
        3. 0003 - Validation Error. Unsupported query combinatio
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/aps/bandwidth_usage/topn"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_switches(access_token, refresh_token):
        """
        List Switch
        Get switches You can only specify one of group, label and stack_id parameters.
        Possible error_codes for the error responses are
        1. 0001 - General Error.
        2. 0002 - Validation Error. Out of Range value for a query parameter.
        3. 0003 - Validation Error. Unsupported query combination
        4. 0004 - Validation Error. Invalid value for a query paramete
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/switches"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_wids_infrastructure_attacks(access_token, refresh_token):
        """
        List Infrastructure Attac
        Get infrastructure attacks over a time perio
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/wids/infrastructure_attacks"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_mobility_controllers_serial_ports(access_token, refresh_token):
        """
        Mobility Controllers Ports Detai
        Get mobility controllers ports details.
        Possible error_codes for the error responses are
        1. 0001 - General Error
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/mobility_controllers/{serial}/ports"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_switches_bandwidth_usage(access_token, refresh_token):
        """
        Switch Bandwidth Usa
        Get switches bandwidth usage over a time period. You can only specify one of group, label, serial and stack_id
        parameters.
        Possible error_codes for the error responses are
        1. 0001 - General Error.
        2. 0002 - Validation Error. Out of Range value for a query parameter.
        3. 0003 - Validation Error. Unsupported query combinatio
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/switches/bandwidth_usage"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_clients_wired_macaddr(access_token, refresh_token):
        """
        Wired Client Detai
        Get wired client detail
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/clients/wired/{macaddr}"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_switches_bandwidth_usage_topn(access_token, refresh_token):
        """
        Top N Switch
        Get top N Switches details over a time period. You can only specify one of group, label and stack_id parameters.
        Possible error_codes for the error responses are
        1. 0001 - General Error.
        2. 0002 - Validation Error. Out of Range value for a query parameter.
        3. 0003 - Validation Error. Unsupported query combinatio
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/switches/bandwidth_usage/topn"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_bssids(access_token, refresh_token):
        """
        List BSSI
        Get a list of BSSIDs. You can only specify one of group, swarm_id, label, serial, macaddr parameters
        Possible error_codes for the error responses are
        1. 0001 - General Error.
        2. 0002 - Validation Error. Out of Range value for a query parameter.
        3. 0003 - Validation Error. Unsupported query combination
        4. 0004 - Validation Error. Invalid value for a query parameter
        5. 0006 - Internal data Error
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/bssids"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_clients_bandwidth_usage(access_token, refresh_token):
        """
        Client Bandwidth Usa
        Get clients bandwidth usage over a time period. You can only specify one of group, swarm_id, label, cluster_id
        and stack_id parameters.
        Possible error_codes for the error responses are
        1. 0001 - General Error.
        2. 0002 - Validation Error. Out of Range value for a query parameter.
        3. 0003 - Validation Error. Unsupported query combinatio
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/clients/bandwidth_usage"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_aps(access_token, refresh_token):
        """
        List Access Poin
        Get access points. You can only specify one of group, swarm_id, label parameters.
        Possible error_codes for the error responses are
        1. 0001 - General Error.
        2. 0002 - Validation Error. Out of Range value for a query parameter.
        3. 0003 - Validation Error. Unsupported query combination
        4. 0004 - Validation Error. Invalid value for a query paramete
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/aps"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_events(access_token, refresh_token):
        """
        List Even
        Get a list of events. You can only specify one of group, swarm_id, label, serial, macaddr parameters.
        Possible error_codes for the error responses are
        1. 0001 - General Error.
        2. 0002 - Validation Error. Out of Range value for a query parameter.
        3. 0003 - Validation Error. Unsupported query combination
        4. 0004 - Validation Error. Invalid value for a query paramete
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/events"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_networks_network_name(access_token, refresh_token):
        """
        Get Network detai
        Get Network details
        Possible error_codes for the error responses are
        1. 0003 - Validation Error. Unsupported query combinatio
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/networks/{network_name}"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_swarms(access_token, refresh_token):
        """
        List Swar
        Get list of swarms. You can optionally specify a group to filter on groups.
        Possible error_codes for the error responses are
        1. 0001 - General Error.
        2. 0002 - Validation Error. Out of Range value for a query parameter.
        3. 0004 - Validation Error. Invalid value for a query paramete
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/swarms"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_vpn_info(access_token, refresh_token):
        """
        Vpn Detai
        Get VPN detail
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/vpn/info"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_switches_serial_chassis_info(access_token, refresh_token):
        """
        Switch Chassis Detai
        Get switch chassis details for chassis type switches.
        Possible error_codes for the error responses are
        1. 0001 - General Error
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/switches/{serial}/chassis_info"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_aps_serial_uplink_history(access_token, refresh_token):
        """
        AP uplink histo
        Get ap uplink history details
        Possible error_code for the error response is
        1. 0002 - Validation Error. Out of Range value for a query parameter
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/aps/{serial}/uplink_history"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_aps_bandwidth_usage(access_token, refresh_token):
        """
        AP Bandwidth Usa
        Get access points bandwidth usage over a time period. You can only specify one of group, swarm_id, label,
        serial, cluster_id parameters.
        Possible error_codes for the error responses are
        1. 0001 - General Error.
        2. 0002 - Validation Error. Out of Range value for a query parameter.
        3. 0003 - Validation Error. Unsupported query combination
        4. 0004 - Validation Error. Invalid value for a query parameter
        5. 0005 - Validation Error. Missing required parameter
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/aps/bandwidth_usage"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_switches_serial(access_token, refresh_token):
        """
        Switch Detai
        Get Switch detail
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/switches/{serial}"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_wids_rogue_aps(access_token, refresh_token):
        """
        List Rogue A
        Get rogue APs over a time perio
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/wids/rogue_aps"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_clients_wireless_macaddr_mobility_trail(access_token, refresh_token):
        """
        Wireless Client Mobility Tra
        Get wireless client mobility details
        Possible error_code for the error response is
        1. 0002 - Validation Error. Out of Range value for a query parameter
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/clients/wireless/{macaddr}/mobility_trail"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_clients_wireless(access_token, refresh_token):
        """
        List Wireless Clien
        Get a list of wireless clients. You can only specify one of group, swarm_id, label parameters.
        Possible error_codes for the error responses are
        1. 0001 - General Error.
        2. 0002 - Validation Error. Out of Range value for a query parameter.
        3. 0003 - Validation Error. Unsupported query combination
        4. 0004 - Validation Error. Invalid value for a query paramete
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/clients/wireless"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_switch_stacks_stack_id_ports(access_token, refresh_token):
        """
        Switch Stack Port Detai
        Get the Port details for a given stack_i
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/switch_stacks/{stack_id}/ports"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_aps_serial_neighbouring_clients(access_token, refresh_token):
        """
        AP Neighbouring Clien
        Get AP neighboring clients over a time period.
        Possible error_codes for the error responses are
        1. 0001 - General Error.
        2. 0002 - Validation Error. Out of Range value for a query parameter.
        3. 0004 - Validation Error. Invalid value for a query paramete
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/aps/{serial}/neighbouring_clients"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_mobility_controllers_serial_ports_bandwidth_usage(access_token, refresh_token):
        """
        Mobility Controllers Ports Bandwidth Usa
        Get Mobility Controller ports bandwidth usage over a time period.
        Possible error_codes for the error responses are
        1. 0001 - General Error.
        2. 0002 - Validation Error. Out of Range value for a query parameter
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/mobility_controllers/{serial}/ports/bandwidth_usage"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_aps_serial_rf_summary(access_token, refresh_token):
        """
        AP RF Summa
        Get AP RF summary of channel utilization, noise floor in positive, errors, drops and retries over a time period.
        Possible error_codes for the error responses are
        1. 0001 - General Error.
        2. 0002 - Validation Error. Out of Range value for a query parameter.
        3. 0004 - Validation Error. Invalid value for a query paramete
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/aps/{serial}/rf_summary"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_central_v1_labels_categories(access_token, refresh_token):
        """
        List Label Catego
        Get a list of label categorie
        """
        url = "https://app1-apigw.central.arubanetworks.com/central/v1/labels/categories"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_mobility_controllers(access_token, refresh_token):
        """
        List Mobility Controlle
        Get mobility controllers. You can only specify one of group, label parameters.
        Possible error_codes for the error responses are
        1. 0001 - General Error.
        2. 0002 - Validation Error. Out of Range value for a query parameter.
        3. 0003 - Validation Error. Unsupported query combination
        4. 0004 - Validation Error. Invalid value for a query paramete
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/mobility_controllers"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_switches_serial_ports_bandwidth_usage(access_token, refresh_token):
        """
        Switch Ports Bandwidth Usa
        Get switch ports bandwidth usage over a time period.
        Possible error_codes for the error responses are
        1. 0001 - General Error.
        2. 0002 - Validation Error. Out of Range value for a query parameter
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/switches/{serial}/ports/bandwidth_usage"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_clients_bandwidth_usage_topn(access_token, refresh_token):
        """
        Top N Clien
        Get top N client details over a time period. You can only specify one of group, swarm_id, label, cluster_id
        and stack_id parameters.
        Possible error_codes for the error responses are
        1. 0001 - General Error.
        2. 0002 - Validation Error. Out of Range value for a query parameter.
        3. 0003 - Validation Error. Unsupported query combinatio
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/clients/bandwidth_usage/topn"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_wids_events(access_token, refresh_token):
        """
        WIDS Even
        Get WIDS events over a time perio
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/wids/events"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_central_v1_labels_associations(access_token, refresh_token):
        """
        WIDS Even
        Get WIDS events over a time perio
        """
        url = "https://app1-apigw.central.arubanetworks.com/central/v1/labels/associations"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_central_v1_labels(access_token, refresh_token):
        """
        List Labe
        Get list of labels
        Possible error_codes for the error responses are
        1. 0001 - General Error.
        2. 0002 - Validation Error. Out of Range value for a query parameter.
        3. 0003 - Validation Error. Unsupported query combination
        4. 0004 - Validation Error. Invalid value for a query paramete
        """
        url = "https://app1-apigw.central.arubanetworks.com/central/v1/labels"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_switches_serial_ports(access_token, refresh_token):
        """
        Switch Ports Detai
        Get switch ports details.
        Possible error_codes for the error responses are
        1. 0001 - General Error
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/switches/{serial}/ports"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_clients_count(access_token, refresh_token):
        """
        Total Clients Cou
        Get the total clients connected
        Possible error_codes for the error responses are
        1. 0001 - General Error.
        2. 0002 - Validation Error. Out of Range value for a query parameter.
        3. 0003 - Validation Error. Unsupported query combination
        4. 0004 - Validation Error. Invalid value for a query paramete
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/clients/count"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_switches_serial_ports_errors(access_token, refresh_token):
        """
        Switch Ports Erro
        Get switch ports error and discards over a time period.
        Possible error_codes for the error responses are
        1. 0001 - General Error.
        2. 0002 - Validation Error. Out of Range value for a query parameter
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/switches/{serial}/ports/errors"
        response = get_central(access_token, refresh_token, url)
        return response


    def get_monitoring_v1_wids_interfering_aps(access_token, refresh_token):
        """
        List Interfering A
        Get interfering APs over a time perio
        """
        url = "https://app1-apigw.central.arubanetworks.com/monitoring/v1/wids/interfering_aps"
        response = get_central(access_token, refresh_token, url)
        return response
