import nmap
import re
import threading

# Regular Expression Pattern to recognise IPv4 addresses.
ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
# Regular Expression Pattern to extract the number of ports you want to scan. 
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
port_min = 0
port_max = 65535

open_ports = []
# Ask user to input the ip address they want to scan.
while True:
    ip_add_entered = input("\nPlease enter the ip address that you want to scan: ")
    if ip_add_pattern.search(ip_add_entered):
        print(f"{ip_add_entered} is a valid ip address")
        break

while True:
    # You can scan 0-65535 ports. This scanner is basic and doesn't use multithreading so scanning 
    # all the ports is not advised.
    print("Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120)")
    port_range = input("Enter port range: ")
    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break

nm = nmap.PortScanner()

def scan_port(ip_address, port):
    try:
        result = nm.scan(ip_address, str(port))
        port_status = (result['scan'][ip_address]['tcp'][port]['state'])
        # print(f"Port {port} is {port_status}")
        if port_status == 'open':
            open_ports.append(port)
    except:
        pass
        # print(f"Cannot scan port {port}.")

# We're looping over all of the ports in the specified range, and scanning each port in a separate thread.
for port in range(port_min, port_max + 1):
    thread = threading.Thread(target=scan_port, args=(ip_add_entered, port))
    thread.start()

# Wait for all threads to finish.
for thread in threading.enumerate():
    if thread != threading.current_thread():
        thread.join()

print(f"Open ports: {open_ports}")
