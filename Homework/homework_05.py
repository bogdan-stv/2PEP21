"""
Create a class for an object that can get the latest stable version of python by downloading and looking in the
content of this page: https://en.wikipedia.org/wiki/History_of_Python
To download the page try using the following command for windows
powershell -c "Invoke-WebRequest -Uri 'https://en.wikipedia.org/wiki/History_of_Python' -OutFile 'C:\temp\page.html'"
or curl, wget, or some other tools you may have in case of mac.
Compare the retrieved version with the first 2 digits of your installed version and show a message to the user
with current and available version
"""

import subprocess
from subprocess import Popen
import os, re, time

class PythonVersion:

    def current_version(self):
        py_version = Popen(['python','--version'],text=True, stdout=subprocess.PIPE)
        stdout = py_version.communicate()[0].split()[1][:3]
        return stdout

    def latest_version(self):
        os.popen("powershell -c \"Invoke-WebRequest"
                 " -Uri \'https://en.wikipedia.org/wiki/History_of_Python\'"
                 " -OutFile \'page.html\'\"")
        while not os.path.isfile("page.html"):
            time.sleep(1)
        with open("page.html", errors='ignore') as page:
            text = page.read()
            result = re.findall(r"Current\sstable\sversion\:\<\/span\>\s\<b\>(\d\.\d)", text)
        return result[0]

check_version = PythonVersion()
print(f"My python version: {check_version.current_version()}")
print(f"Latest stable version: {check_version.latest_version()}")
