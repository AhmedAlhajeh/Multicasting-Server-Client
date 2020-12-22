import socket
import time

MulticastPort = 10000
MulticastAddress = '224.3.29.71'
AnyIPAddress = '127.0.0.1'
IPPort = 1501

message = "Multicasting Assignment ECE 4436 from Server 1"
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#Creating socket for server
sock.bind((AnyIPAddress,IPPort))#making sure the data is sent from 127.0.0.1 and port number 1501
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 255) #define packet TTL = 225
while 1:
    time.sleep(3) #send multicast message every 3 seconds
    sock.sendto(message.encode(encoding='utf_8'),(MulticastAddress,MulticastPort)) #sending the actual message to address 127.0.0.1 and port 1600
    print('Server 1 : multicast packet is sent now') #printing messages that the packet is being sent to client