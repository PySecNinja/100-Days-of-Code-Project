"""
USAGE - This code imports the scapy module and the re module. It defines a 
        regular expression pattern to recognize IPv4 addresses and prompts 
        the user to enter an IP address range. It then uses the scapy.arping() 
        function to send an Address Resolution Protocol (ARP) request to the
        specified IP address range.

AUTHOR - https://github.com/Ahendrix9624/
"""

import scapy.all as scapy
import re

# Regular Expression Pattern to recognise IPv4 addresses.
ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

# Get the address range to ARP
while True:
    ip_add_range_entered = input("\nPlease enter the ip address and range that you want to send the ARP request to (ex 192.168.1.0/24): ")
    if ip_add_range_pattern.search(ip_add_range_entered):
        print(f"{ip_add_range_entered} is a valid ip address range")
        break

arp_result = scapy.arping(ip_add_range_entered)