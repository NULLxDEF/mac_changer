#!/usr/bin/env python

import subprocess  # To execute system commands
import optparse    # To handle command-line options and arguments
import re          # For regular expression operations

def get_arguments():
    # Parse command-line arguments for interface and new MAC address
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    
    # Extract options and validate them
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a NEW MAC, use --help for more info.")
    return options

def change_mac(interface, new_mac):
    # Change the MAC address of the specified network interface
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])  # Bring the interface down
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])  # Change the MAC address
    subprocess.call(["ifconfig", interface, "up"])  # Bring the interface up

def get_current_mac(interface):
    # Retrieve the current MAC address of the specified network interface
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result.decode("utf-8"))

    if mac_address_search_result:
        return mac_address_search_result.group(0)  # Return the first matched MAC address
    else:
        print("[-] Could not read MAC address.")

# Retrieve command-line options
options = get_arguments()

# Display the current MAC address before attempting to change it
current_mac = get_current_mac(options.interface)
print("[+] Current MAC >>> " + str(current_mac))

# Change the MAC address
change_mac(options.interface, options.new_mac)

# Verify and display the MAC address after the change
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address was successfully changed to " + current_mac)
else:
    print("[-] MAC address did not get changed.")

