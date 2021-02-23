#!/usr/bin/env python3
# private classes
from cisco import show_cmd_ssh
# show_cmd_ssh(hostname, username, password, command): 

device_ip = input("device name? ")
user_name = input("username: ")
device_password = input("device password: ")
filename = input("Filename for commands to run: ")

list_of_commands = []
with open(filename) as read_file:
    for line in read_file:
        list_of_commands.append(line.strip('\n'))
print(list_of_commands)

with open(f"{device_ip}", "w") as file:
    for command in list_of_commands:
        result = show_cmd_ssh(device_ip, user_name, device_password, command)
        file.write('\n' + command + "\n")
        for data in result:            
            file.write(data.strip('\r\n'))
            file.write("\n")



