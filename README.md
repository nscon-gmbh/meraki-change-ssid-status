# meraki-shut-wifi

Shutdown a specific wireless SSID via Meraki Dashboard API.

## Use Case Description

A customer had the request to quickly shutdown a specific SSID which was available on all Meraki site networks.

## Installation

> **Note:** This installation was done on macOS Monterey 12.6 using Python 3.9.13. I recommend using a Linux or Unix based machine.

1. Clone the repository and change into new directory:

    ```bash
    git clone https://github.com/nscon-gmbh/meraki-shut-wifi.git`
    cd meraki-shut-wifi
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

Enter the search string for the SSID(s) you want to shutdown. Be as specific as you can:

```bash
python meraki_shutdown_ssid.py <SSID search string>
```

Example output:

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

Found "TEST" in the following enabled SSIDs:

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

Changed status of the following enabled SSIDs:

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

### DevNet Sandbox

You can test the script at the [Meraki Small Business DevNet Sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/86cdf547-27ba-43f3-81a7-9c22f57cdf28).

## How to test the software

Provide details on steps to test, versions of components/dependencies against which code was tested, date the code was last tested, etc. 
If the repo includes automated tests, detail how to run those tests.
If the repo is instrumented with a continuous testing framework, that is even better.


## Known issues

Document any significant shortcomings with the code. If using [GitHub Issues](https://help.github.com/en/articles/about-issues) to track issues, make that known and provide any templates or conventions to be followed when opening a new issue.

## Getting help

Instruct users how to get help with this code; this might include links to an issues list, wiki, mailing list, etc.

**Example**

If you have questions, concerns, bug reports, etc., please create an issue against this repository.

## Getting involved

This section should detail why people should get involved and describe key areas you are currently focusing on; e.g., trying to get feedback on features, fixing certain bugs, building important pieces, etc. Include information on how to setup a development environment if different from general installation instructions.

General instructions on _how_ to contribute should be stated with a link to [CONTRIBUTING](./CONTRIBUTING.md) file.

## Author(s)

This project was written and is maintained by the following individuals:

* Daniel Kuhl <kuhl@nscon.de>
