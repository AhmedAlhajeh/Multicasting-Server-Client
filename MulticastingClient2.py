import socket



MulticastPort2 = 10000
MulticastAddress2 = '224.3.29.71'
AnyIPAddress2 = '127.0.0.1'

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #Creating socket for client
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #we can use each socket address more than once becasue we have two clients
sock.bind((AnyIPAddress2,MulticastPort2))#making sure the data is received from 127.0.0.1 and port number 10000
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 255) #define packet TTL = 225
status = sock.setsockopt(socket.IPPROTO_IP,socket.IP_ADD_MEMBERSHIP,socket.inet_aton(MulticastAddress2)+socket.inet_aton(AnyIPAddress2))



while 1:
    try:
        data,address = sock.recvfrom(4096)
    except socket.error:
        pass
    else:
        print("Client 2 : Data Received from:", address)
        print("and the Received Data is: ",data)
