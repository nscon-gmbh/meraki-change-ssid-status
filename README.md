# Meraki change SSID status

[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/nscon-gmbh/meraki-change-ssid-status)

[![Run in VSCode](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-runable-icon.svg)](https://developer.cisco.com/devenv/?id=devenv-vscode-base&GITHUB_SOURCE_REPO=https://github.com/nscon-gmbh/meraki-change-ssid-status)

Change the status of wireless SSIDs via Meraki Dashboard API.

## Use Case Description

A customer had the request to quickly disable a specific SSID which was available on all Meraki site networks. The script searches through the networks of a chosen organization for the specified search string and returns the results of SSIDs found. Then you can choose if you want to change the status from enabled to disable or from disable to enable. A table with the results after the change will be provided at the end.

## Installation

> **Note:** This installation was done on macOS Monterey 12.6 using Python 3.9.13. I recommend using a Linux or Unix based machine.

1. Clone the repository and change into new directory:

    ```bash
    git clone https://github.com/nscon-gmbh/meraki-change-ssid-status.git
    cd meraki-change-ssid-status
    ```

2. Create and activate virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install Python modules used in the script:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

There is no need for any further configuration. It is optional to use your Meraki API key as environment variable called "YOUR_MERAKI_API_KEY" in the script. Otherwise you will get a prompt to paste your API key during execution of the script. All log files from the Meraki Dashboard API will be stored at the "logs" folder.

Make sure to have a valid Meraki API key. Please check the [Meraki Dashboard API documentation](https://developer.cisco.com/meraki/api-v1/) for any further information.

## Usage

Enter the search string for the SSID(s) you want to change:

```bash
python meraki-change-ssid-status.py <SSID search string>
```

Be as specific as you can with your search string. You should be close to the SSID name you want to change. If the results for your change are not sufficient then press "n" for no and there will be no status change.

**Example output:**

```bash
(venv) $ python meraki_shutdown_ssid.py TEST

INFO: For log files please check the "logs" folder.

Your API Key grants access to the following orgs:

╒═══════╤═══════════════╤══════════╕
│   No. │ Org Name      │   Org ID │
╞═══════╪═══════════════╪══════════╡
│     0 │ Company 123   │   123456 │
├───────┼───────────────┼──────────┤
│     1 │ Customer xyz  │   789012 │
╘═══════╧═══════════════╧══════════╛

Choose one org no. from list: 0

Searching for "TEST" in SSID "SSID 123" in network "Network 123"...

Searching for "TEST" in SSID "SSID TEST" in network "Network 123"...

Searching for "TEST" in SSID "WIFI TEST" in network "Network TEST"...

ERROR: Skipping search for "TEST" in network "Network PROD"...

Found "TEST" in the following SSIDs:

╒═══════╤════════════════╤═══════════╤════════════╤═══════════╕
│   No. │ Network Name   │ SSID Name │   SSID No. │ Enabled   │
╞═══════╪════════════════╪═══════════╪════════════╪═══════════╡
│     0 │ Network 123    │ SSID 123  │          0 │ True      │
├───────┼────────────────┼───────────┼────────────┼───────────┤
│     1 │ Network 123    │ SSID TEST │          1 │ True      │
├───────┼────────────────┼───────────┼────────────┼───────────┤
│     2 │ Network TEST   │ WIFI TEST │          1 │ True      │
╘═══════╧════════════════╧═══════════╧════════════╧═══════════╛

Change status of all found SSIDs? (y/n) y

Changed status of the following SSIDs:

╒═══════╤════════════════╤══════════════════╤════════════════════╤═══════════════════╕
│   No. │ Network Name   │ SSID Name        │ Enabled (before)   │ Enabled (after)   │
╞═══════╪════════════════╪══════════════════╪════════════════════╪═══════════════════╡
│     0 │ NSCON TEST     │ NSCON TEST       │ True               │ False             │
├───────┼────────────────┼──────────────────┼────────────────────┼───────────────────┤
│     1 │ NSCON TEST     │ NSCON TEST 2     │ True               │ False             │
├───────┼────────────────┼──────────────────┼────────────────────┼───────────────────┤
│     2 │ NSCON HO DK    │ Nautomation TEST │ True               │ False             │
╘═══════╧════════════════╧══════════════════╧════════════════════╧═══════════════════╛
```

## How to test the software

To test the script please use the [Meraki Small Business DevNet Sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/86cdf547-27ba-43f3-81a7-9c22f57cdf28) and follow the instructions provided for the sandbox setup as well as for configuration and usage on this page.

> **Note:** You have only read-write access to a specific network on this DevNet sandbox organization which is named with your email address you reserved it at the end of the name of the network.

## Known issues

There are currently no known issues. Please use [GitHub Issues](https://github.com/nscon-gmbh/meraki-quick-check/issues) to open a new issue by providing a helpful description about the issue.

## Getting help

If you have questions, concerns, bug reports, etc., please create an issue against this repository or get in contact with the author.

## Getting involved

Please get involved by giving feedback on features, fixing certain bugs, building important pieces, etc.

## Author(s)

This project was written and is maintained by the following individuals:

* Daniel Kuhl <kuhl@nscon.de>
