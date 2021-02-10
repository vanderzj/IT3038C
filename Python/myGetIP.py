import socket, sys

def getHostNameByIP(h):
    try:
        hostname = str(h)
        ip = socket.gethostbyname(hostname)
        print(hostname + " has an IP Address of " + ip)
    except:
        print("Invalid Hostname")

getHostNameByIP(sys.argv[1])