import nmap

ip = '192.168.1.2'
nm = nmap.PortScanner()
scan_result = nm.scan(ip)
for information in scan_result:
    print(information)