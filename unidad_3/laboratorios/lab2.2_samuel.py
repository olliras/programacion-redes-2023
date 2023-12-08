
'''Nombre: Samuel Reynaldo Olvera Lira
   lab: 2.2
   fecha: 24 Nov 2023
'''


from netmiko import ConnectHandler


device_params = {
    'device_type': 'cisco_ios',
    'host': '10.10.20.48',
    'port': 22,
    'username': 'developer',
    'password': 'C1sco12345',
}


sshCli = ConnectHandler(**device_params)
salida = sshCli.send_command('show ip interface brief')
print(salida)


config_commands = [
    'interface loopback 1',
    'ip address 2.2.2.2 255.255.255.0',
    'description WHATEVER',
]

output = sshCli.send_config_set(config_commands)


show_ip_output = sshCli.send_command('show ip interface brief')
print(" loopback1:")




config_commands = [
    'interface loopback 2',
    'ip address 2.2.2.2 255.255.255.0',
    'description NEW',
]

output = sshCli.send_config_set(config_commands)


show_ip_output = sshCli.send_command('show ip interface brief')
print(" looback 2:")


