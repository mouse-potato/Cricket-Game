from socket import *
serverport=1200
serversocket=socket(AF_INET,SOCK_DGRAM)
serversocket.bind(('',serverport))
#serversocket.listen(1)
while(1):
	#connectionsocket,addr=serversocket.accept()
	sentence,addr=serversocket.recvfrom(2048)
	sentence=sentence.decode('utf8')
	print(sentence)
	reply=input()
	#print(sentence)
	send=(bytes(str(reply),'utf8'))
	serversocket.sendto(send,addr)
	




