
import socket
import time

MulticastPort2 = 10000
MulticastAddress2 = '224.3.29.71'
AnyIPAddress2 = '127.0.0.1'
IPPort2 = 1502

message = "Multicasting Assignment ECE 4436 from Server 2"
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#Creating socket for server
sock.bind((AnyIPAddress2,IPPort2))#making sure the data is sent from 127.0.0.1 and port number 1502
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 255) #define packet TTL = 225
while 1:
    time.sleep(3) #send multicast message every 3 seconds
    sock.sendto(message.encode(encoding='utf_8'),(MulticastAddress2,MulticastPort2)) #sending the actual message to address 127.0.0.1 and port 1600
    print('Server 2 : multicast packet is sent now') #printing messages that the packet is being sent to client