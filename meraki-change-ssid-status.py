#!/usr/bin/env python
"""Import Python modules."""

import os
import sys
import argparse
import tabulate
import meraki


def get_org(dashboard):
    """Function to get organization id."""

    # Define table headers and values for organizations
    headers = ["No.", "Org Name", "Org ID"]
    table = []

    # Get all organizations
    try:
        orgs = dashboard.organizations.getOrganizations()

        # If more than one organization then get all org data and print table
        i = 0
        if len(orgs) > 1:
            print('\nYour API Key grants access to the following orgs:\n')
            for org in orgs:
                org_name = orgs[i]['name']
                org_id = orgs[i]['id']
                i += 1

                # Add all organization data to table row and add row to table
                row = [org_name, org_id]
                table.append(row)

            # Print table using the received organization data
            print(tabulate.tabulate(
                table, headers=headers, tablefmt='fancy_grid', showindex=True
                )
            )

            # Choose organization number from table
            org_no = int(input('\nChoose one org no. from list: '))
            org = table[org_no]

            # Get organization details and assign variables
            org_id = org[1]
            org_name = org[0]

        # Else choose the only organization available
        else:
            org = orgs[0]

            # Get organization details and assign variables
            org_id = org.get('id')
            org_name = org.get('name')

    except meraki.exceptions.APIError as error:
        print(f'\nERROR: {error}')
        org_id = input('\nPlease enter your org ID manually: ')

    return org_id


def get_ssids(dashboard, org_id):
    """Function to get ssids."""

    # Get list of networks for organization
    networks = dashboard.organizations.getOrganizationNetworks(org_id)

    # Define table headers and values for ssids
    ssid_data = {}
    headers = ['No.', 'Network Name', 'SSID Name', 'SSID No.', 'Enabled']
    table = []

    # Iterate through network_list and print networks
    for network in networks:
        network_id = network['id']
        network_name = network['name']

        # Get all ssids for given network_id
        ssids = {}
        ssid_list = []
        i = 0

        try:
            ssid_list = dashboard.wireless.getNetworkWirelessSsids(network_id)

            # Loop through list of ssids and set variables
            for ssid_name in ssid_list:
                ssid_name = ssid_list[i]['name']
                ssid_status = ssid_list[i]['enabled']
                ssid_number = ssid_list[i]['number']

                print(f'\nSearching for "{ssid_search}" in SSID ' +
                      f'"{ssid_name}" in network "{network_name}"...')

                if ssid_search in ssid_name:
                    # Add all ssid data to table row and add row to table
                    row = [network_name, ssid_name, ssid_number, ssid_status]
                    table.append(row)

                    ssids[ssid_name] = [network_name, ssid_number, ssid_status]
                    ssid_data[network_id] = ssids

                i += 1

        except meraki.exceptions.APIError:
            print(f'\nERROR: Skipping search for "{ssid_search}" ' +
                  f'in network "{network_name}"...')

    # Print table using the received data
    print(f'\nFound "{ssid_search}" in the following enabled SSIDs:\n')
    print_ssids(table, headers)

    return ssid_data


def change_ssid_status(dashboard, ssid_data):
    """Function to get ssid status."""

    # Define table headers and values for ssids
    headers = [
        'No.',
        'Network Name',
        'SSID Name',
        'Enabled (before)',
        'Enabled (after)'
        ]
    table = []

    # Set change variable to True
    change = True

    # Iterate through ssid data and disable ssids
    for network_id, values in ssid_data.items():
        for ssid_name, ssid_details in values.items():
            network_name = ssid_details[0]
            ssid_number = ssid_details[1]
            ssid_status = ssid_details[2]

            # If ssid is enabled then diable, if disabled then enable
            if ssid_status is True:
                change = False

            result = dashboard.wireless.updateNetworkWirelessSsid(
                network_id, ssid_number,
                name=ssid_name,
                enabled=change
            )

            # Update SSID status
            ssid_status_updated = result['enabled']

            # Add all ssid data to table row and add row to table
            row = [
                network_name,
                ssid_name,
                ssid_status,
                ssid_status_updated
                ]
            table.append(row)

    # Print table using the received data
    print('\nChanged status of the following enabled SSIDs:\n')
    print_ssids(table, headers)


def print_ssids(table, headers):
    """Function to get ssid status."""

    print(tabulate.tabulate(
        table,
        headers=headers,
        tablefmt="fancy_grid",
        showindex=True
        )
    )


# Enter SSID to shutdown with argument
parser = argparse.ArgumentParser()
parser.add_argument("search", type=str,
                    help="enter string to search in the ssid")
args = parser.parse_args()
ssid_search = args.search

# Check if folder 'logs' exists otherwise create it
if os.path.exists('logs'):
    print('\nINFO: For log files please check the "logs" folder.')
else:
    print('\nINFO: Log folder not found - creating "logs" folder for you.')
    os.mkdir('logs')

# Set Meraki API Key via env variable or input if not set
try:
    api_key = os.environ.get('YOUR_MERAKI_API_KEY')
except KeyError:
    api_key = input('\nEnter your Meraki API key: ')

# Set API call, send logs to log folder and omit log output on console
connect = meraki.DashboardAPI(api_key, log_path="logs", print_console=False)

# Call function to get org id
organization = get_org(connect)

# Call function to get ssids with search string
data = get_ssids(connect, organization)

if input('\nChange status of all found SSIDs? (y/n) ') != 'y':
    sys.exit()

# Call function to het ssid status
change_ssid_status(connect, data)
