import subprocess
import re
# allows use of regular expressions

command_output = subprocess.run(["netsh", "wlan", "show", "profiles"],capture_output=True).stdout.decode()
profile_names =(re.findall("All users Profiles  :(.*)\r", command_output))
  #creates a list dic where all wifis available will be stored outside the loop.
wifi_list = list()
 # then  we create if_arguements to take care of the possibilities that wifis might not be in range and also check their passwords and user names.
if len( profile_names) !=0:
    for name in profile_names:
        wifi_profile = dict()
        profile_info =subprocess.run(["netsh","wlan", "show", "profiles", name], capture_output=True).stdout.decode()
        if re.search("security key  :Absent", profile_info ):  # this is the instance when the wifi doesnt have a password.
            continue
        else:
            wifi_profile["ssid"] = name    #.. we assign the ssid profile to the name instead.
            profile_info_pass = subprocess.run (["netsh", "wlan", "show", "profiles", name, "key=clear"], capture_output=True).stdout.decode()
            # in the incidences where the wifi has a password, key=clear command allows you to see the password.
            password = re.search("Key Content   :(.*)\r", profile_info_pass)
            # then now we chsck if found a password or their is none.
            if password == None:
                wifi_profile["password"] = None
            else :
                wifi_profile["password"] = password[1]    # then we attach the wifi password to the wifi list.
            wifi_list.append(wifi_profile)
for x in range(len(wifi_list)):
    print(wifi_list[x])





