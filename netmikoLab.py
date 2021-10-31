import os
from netmiko import ConnectHandler
from getpass import getpass
from netmiko.ssh_exception import AuthenticationException, SSHException, NetMikoTimeoutException

USERNAME = input("Enter your SSH username: ")
PASSWORD = getpass("Enter your SSH password: ")

device = {
    'ip': '192.168.0.0',
    'username': USERNAME,
    'password': PASSWORD,
    'device_type': 'cisco_ios'
}

import os
from netmiko import ConnectHandler
from getpass import getpass
from netmiko.ssh_exception import AuthenticationException, SSHException, NetMikoTimeoutException

USERNAME = input("Enter your SSH username: ")
PASSWORD = getpass("Enter your SSH password: ")

device = {
    'ip': '192.168.0.0',
    'username': USERNAME,
    'password': PASSWORD,
    'device_type': 'cisco_ios'
}

try:
    c = ConnectHandler(**device)
    output = c.send_command('show run')
    f = open('backup.conf', 'x')
    f.write(output)
    f.close()
except (AuthenticationException):
    print("An authentication error occured while connecting to: " + device['ip'])
except (SSHException):
    print("An error occured while connecting to device " + device['ip'] + " via SSH. Please check if SSH is enabled.")
except (NetMikoTimeoutException):
    print("The device " + device['ip'] + "timed out when attempting to connect")

    
