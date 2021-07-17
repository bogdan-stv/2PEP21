"""Create a class for an object that can:
 - continually monitor the cpu usage and send send alert when usage is over 50%
 - get data about de cpu in dictionary format only for keys that have a value
 -
"""

import os, re

class CpuChecker:

    def monitor_usage(self):
        output = str(os.popen("wmic cpu get loadpercentage").readlines())
        match = re.search(r"\d{1,3}", output)
        print(match.group(0))
        if int(match.group(0)) < 50:
            with open("alert.txt", "w") as alert:
                alert.write(f"Your cpu usage is {match.group(0)}")
            os.popen("notepad.exe alert.txt")

    def data(self):
        output = (str(os.popen("wmic cpu get").readlines()))
        matches = re.findall(57 * r"(\w+\s+)", output)
        matches2 = re.findall(r"(,\s')"+r"(([\S]+\s){1,8}\s+)" * 42, output)
        for match2 in matches2[0]:
            print(match2)
        new_dict = {}
        for match in matches[0]:
            new_dict[match] = None



checker = CpuChecker()
string = (str(os.popen("wmic cpu get").readlines()))
print(string)
match = re.findall(r"\w+", string)
for x in match:
    print(x)
#checker.monitor_usage()
#checker.data()