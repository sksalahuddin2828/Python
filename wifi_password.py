import cmd
from distutils.cmd import Command
import subprocess
import re

command = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()
profiles = (re.findall("All User Profile     : (.*)\r", command))
WifiList = []

if len(profiles) != 0:
    for name in profiles:
        WifiProfile = {}
        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output = True).stdout.decode()
        if re.search("Security key           : Absent", profile_info):
            continue
        else:
            WifiProfile["ssid"] = name
            profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode()
            __password__ = re.search("Key Content            : (.*)\r", profile_info_pass)
            if __password__ == None:
                WifiProfile["password"] = None
            else:
                WifiProfile["password"] = __password__[1]
            WifiList.append(WifiProfile) 

for x in range(len(WifiList)):
    print(WifiList[x])
