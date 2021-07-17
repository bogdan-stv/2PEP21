"""
Create a class for an object that can retrieve:
 - IP address from each interface on teh system and provide it as a dictionary ex: {'INTERFACE_NAME': 192.168.0.1}
        use command ipconfig (windows) or ifconfig (linux/macOS)
 - IPv4 Route Table as a list of dictionaries. ex: [{'Network Destination': '0.0.0.0', 'Gateway': 192.168.0.1 ...}, {Network...}]
        use command route print (windows) route -n (linux/macOS)
"""

import os, re

class Regex:

    def retrieve_ip(self):
        output = str(os.popen("ipconfig").readlines())
        matches = re.finditer(r'(Ethernet|Wireless)(\s\w+)+', output)
        interfaces = []
        for match in matches:
            interfaces.append(match.group())
        ip_matches = re.finditer(r"disconnected|(?<=(Address. . . . . . . . . . . : ))(\d+\.)+\d+", output)
        ip_adresses = []
        for ip_match in ip_matches:
            ip_adresses.append(ip_match.group())
        dict = {interfaces[i] : ip_adresses[i] for i in range(len(interfaces))}
        return dict

    def route_table(self):
        output = str(os.popen("route print").readlines())
        matches = re.finditer(r"(\d+\.)+\d+|On-link|\d{2,3}(?=\\n)", output)
        i, values = 0, []
        for match in matches:
            if i < 80:
                values.append(match.group())
                i += 1
        keys = ["Network Destination", "Netmask", "Gateway", "Interface", "Metric"]
        dict = {k: None for k in keys}
        list = []
        x = 0
        for _ in range(16):
            for key in keys:
                dict[key] = values[x]
                x += 1
            list.append(dict.copy())
        return list


regex = Regex()
print(f"\n\n{regex.retrieve_ip()}\n\n")
list = regex.route_table()
for x in list:
    print(x)

