from netmiko import ConnectHandler

router_info = {
    'device_type': 'cisco_ios',
    'host':   '192.168.10.10',
    'username': 'ansi',
    'password': '123',
    'port' : 22
}

def make_connect(router):
    net_connect = ConnectHandler(**router)
    return net_connect

if __name__ == "__main__":
    net_connect = make_connect(router_info)
    output = shownet_connect.send_command('show ip int brief')
