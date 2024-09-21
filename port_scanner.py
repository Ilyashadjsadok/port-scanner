import socket
import sys
from datetime import datetime


def check_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        #print("invalid IP address ex: X.X.X.X and 0<=X<=255")
        return False
    for part in parts:
        # Check if it's a digit and between 0 and 255
        if not part.isdigit() or not (0 <= int(part) <= 255):
            return False

def get_port_info(p):
    try:
        service = socket.getservbyport(p)
        print(f"Port {p} is used for the service: {service}")
    except OSError:
        print(f"No service information available for port {p}")


#define targets and check their validity
if len(sys.argv) == 2:
    if check_ip(sys.argv[1]) == 0:
        print("invalid IP address, correct form is X.X.X.X and 0<=X<=255")
        sys.exit()
    target = socket.gethostbyname(sys.argv[1])
    #print('Inserted target is a domain name, IP: '+str(target))
else:
    print('invalid amount of args')
    print('correct syntax is: python3 port_scanner.py <Target IP>')
    sys.exit()

#Scanning
print("=*"*25)
print('scanning target: '+str(target))
print('Time started: '+ str(datetime.now()))
print("=*"*25)
try:
    for port in range(1,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print(f"Port {port} is open")
            get_port_info(port)
        s.close()

#exceptions used to quit the program:
except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()
print('Time ended: '+ str(datetime.now()))
