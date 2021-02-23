#!/usr/bin/env python3
# private classes
from cisco import show_cmd_ssh
# show_cmd_ssh(hostname, username, password, command): 

class TshootBackend:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def get_config(self, list_of_commands, list_of_devices):
        device_output = {}
  
        for device in list_of_devices:
            outputs = []
            for command in list_of_commands:
                if not show_cmd_ssh(device, self.username, self.password, command):
                    return False
                for data in show_cmd_ssh(device, self.username, self.password, command):
                    outputs.append(data.strip('\r\n'))
            device_output[device] = outputs
        return device_output

# user_name = input("username: ")
# password = input("password: ")
# print(user_name, password)
# list_of_commands = input("List of Commands (python list): ").split(",")
# list_of_devices = input("List of devices (python list): ").split(",")
# tshoot = TshootBackend(user_name, password)


device_ip = input("device name? ")
device_password = input("device password: ")
list_of_commands = [
    'term length 0',
    'show mpls ldp discovery',
    'show mpls ldp neighbor detail',
    'show run | inc session protection',
    'show mpls ldp nei | inc Target'
]
with open(f"{device_ip}", "w") as file:
    for command in list_of_commands:
        result = show_cmd_ssh(device_ip, "qadirs", device_password, command)
        file.write('\n' + command + "\n")
        for data in result:            
            file.write(data.strip('\r\n'))
            file.write("\n")



