import nmap

ip = '192.168.2.39'
nm = nmap.PortScanner()
print(nm.scan(ip, '-O'))

# if 'osmatch' in nm[ip]:
# for osmatch in nm[ip]['osmatch']:
#     print('----------------')
#     print('name: %s' % osmatch['name'])
#     print('accuracy: %s' % osmatch['accuracy'])
#     print('line: %s' % osmatch['line'])
#     if 'osclass' in osmatch:
#         for osclass in osmatch['osclass']:
#             print('type: %s' % osclass['type'])
#             print('vendor: %s' % osclass['vendor'])
#             print('osfamily: %s' % osclass['osfamily'])
#             print('osgen: %s' % osclass['osgen'])
#             print('accuracy: %s' % osclass['accuracy'])                
