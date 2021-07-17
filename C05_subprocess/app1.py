"""
* get IP address from OS
"""
import subprocess, re, time, os
from subprocess import Popen, run

class Utils:

    def ip_adress(self):
        result = Popen(['ipconfig'], text=True, stdout=subprocess.PIPE)
        output = result.communicate()[0]
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

    def connect_ssh(self, ip):
        result = Popen(['ssh', ip], shell=True)
        output = result.communicate()[0]

    def allow_user_to_enter_message(self):
        notepad = Popen(['notepad.exe', 'file.txt'])
        time.sleep(3)
        # notepad.communicate(input='hello')
        notepad.terminate()

    def ping(self, ip_address):
        ping_var = Popen(['ping', ip_address], stderr= subprocess.PIPE)
        try:
            stdout, stderr = ping_var.communicate(timeout=10)
        except subprocess.TimeoutExpired:
            ping_var.terminate()
            stdout, stderr = ping_var.communicate()
        print(f"Errors: {stderr}")

    # cat /var/log/wifi.log | grep ERROR
    def search_for_erors(self, level='ERROR', path=''):
        if os.path.isfile(path):
            cat = Popen(['cat', path], stdout=subprocess.PIPE)
        if os.path.isdir(path):
            output = run(['dir'], shell=True, text=True, capture_output=True, cwd=path)
            files = output.stdout
            output2 = re.search(files, r"\d+\/\d+\/\d+\s+\d+:\d+\s\w+\s+(\d+,?){0,5}\s(?P<file>.*)")
            print(output2)
        # cat = Popen(['cat', '/var/log/wifi.log'], stdout= subprocess.PIPE)
        # grep = Popen(['grep', level], stdin = cat.stdout, stdout=subprocess.PIPE)
        # cat.stdout.close()
        # output = grep.communicate()[0]
        # print(output)


utils = Utils()
# print(utils.ip_adress())
# utils.connect_ssh('20.52.179.60')
# utils.allow_user_to_enter_message()
# utils.ping('8.8.8.8')
utils.search_for_erors(path='C:\\MinGW\\bin')



