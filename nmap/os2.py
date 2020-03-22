import nmap

ip = '192.168.1.2'
nm = nmap.PortScanner()
information = nm.scan(ip)
print(information)