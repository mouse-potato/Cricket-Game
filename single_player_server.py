import random
from socket import *
serverport=1200
serversocket=socket(AF_INET,SOCK_STREAM)
serversocket.bind(('',serverport))
serversocket.listen(1)
while(1):
	connectionsocket,addr=serversocket.accept()
	generate=random.randint(1,6)
	print(generate)
	connectionsocket.send(bytes(str(generate),'utf8'))
	
#connectionsocket.close()
