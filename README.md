# MAC Changer

This Python script allows you to change the MAC address of a specified network interface on a Linux system. Changing your MAC address can help with privacy and security, as well as testing and troubleshooting network configurations.

## Features

- Change the MAC address of any network interface.
- Verify the MAC address before and after changing it.
- Simple command-line interface.

## Prerequisites

- Python 3.x
- Linux system with `ifconfig` command available
- `venv` (Python Virtual Environment)

## Setup

1. Clone this repository:

    ```bash
    git clone https://github.com/NULLxDEF/mac_changer.git
    cd mac_changer
    ```

2. Create and activate the virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install any necessary dependencies (if applicable):

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To change the MAC address of a network interface, follow these steps:

1. Ensure you are in the virtual environment:

    ```bash
    source venv/bin/activate
    ```

2. Run the script with sudo:

    ```bash
    sudo python3 mac_changer.py -i <interface> -m <new_mac_address>
    ```

   Replace `<interface>` with the network interface you want to change (e.g., `eth0`, `wlan0`), and `<new_mac_address>` with the desired MAC address (e.g., `00:11:22:33:44:55`).

## Example

```bash
sudo python3 mac_changer.py -i wlan0 -m 00:11:22:33:44:55
