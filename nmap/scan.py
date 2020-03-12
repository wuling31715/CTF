import nmap

nm = nmap.PortScanner()
ip = input()
nm.scan(ip, '1-1000')
print(nm.all_hosts())
for host in nm.all_hosts():
    print('-----------------')
    print('host: %s' % host)
    print('hostname: %s' % nm[host].hostname())
    print('state: %s' % nm[host].state())
