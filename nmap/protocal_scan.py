import nmap

ip = '192.168.1.0/24'
port = '80'
nm = nmap.PortScanner()
nm.scan(ip, port)
for host in nm.all_hosts():
    print('---------------')
    print('host: %s' % host)
    print('hostname: %s' % nm[host].hostname())
    print('state: %s' % nm[host].state())
    for protocol in nm[host].all_protocols():
        print()
        print('protocal: %s' % protocol)
        port = list(nm[host][protocol].keys())
        print(port)