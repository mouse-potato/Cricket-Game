from socket import *



	
	

def connection1(ipadd,message):
	
	
	servername=ipadd
	serverport=1200
	clientsocket=socket(AF_INET,SOCK_STREAM)
	clientsocket.connect((servername,serverport))
	choice=message
	clientsocket.send(bytes(str(choice),'utf8'))
	
		
	x=clientsocket.recv(1224)
	x=x.decode('utf8')
	clientsocket.close()
	return int(x)
	
def connection(ipadd,message):

	servername=ipadd
	serverport=1200
	clientsocket=socket(AF_INET,SOCK_DGRAM)
	clientsocket.connect((servername,serverport))
	choice=message
	clientsocket.sendto(bytes(str(choice),'utf8'),(servername,serverport))
		
	x=clientsocket.recv(12000)
	x=x.decode('utf8')
	clientsocket.close()
	return int(x)

	
	

def batting1st(ipadd):
	totalrun=0
	wicket=0
	ballcount=0
	while(ballcount!=12 and wicket!=5):
		#print("choice")
		bat=int(input())
		#print("after")
		while(runcheck(bat)==0):
			print("invalid run")
			bat=int(input())
			
		bowl=connection(ipadd,"Enter your Number\n")
	
		#print(bowl)
		if(bat==bowl):
			print("OUT")
			wicket+=1
			print("Wicket remaining",5-wicket)
			print("Runs scored",totalrun)
			connection(ipadd,"OUT\n")
			mw=wicket
			mr=totalrun
			#connection(ipadd,"wicket"+str(mw))
			#connection(ipadd,"run"+str(mr))
		else:
			totalrun+=bat
		ballcount+=1
		#print(ballcount)
		if(ballcount%6==0):
			mb=ballcount//6
			mr=totalrun
			mw=wicket
			print("end of over",ballcount//6)
			print( "totalruns",totalrun,"wickets lost",wicket)
			#connection(ipadd,"wicket"+str(mw))
			#connection(ipadd,"run"+str(mr))
			connection(ipadd,"Overs"+str(mb)+"\n")
		
	
	print(totalrun)
	connection(ipadd,"total run scored"+str(totalrun)+"\n")
	return totalrun



def batting2nd(ipadd,x):
	totalrun=0
	wicket=0
	ballcount=0
	while(ballcount!=12 and wicket!=5):
		bat=int(input())
		while(runcheck(bat)==0):
			print("invalid run")
			bat=int(input())
		bowl=connection(ipadd,"Enter your Number")
		if(bat==bowl):
			print("OUT")
			connection(ipadd,"OUT")	
			wicket+=1
			if(wicket==5):
				print("YOU WON")
				connection(ipadd,"YOU LOST")	
				return 0
			mr=totalrun
			mw=wicket
			connection(ipadd,"wicket"+str(mw))
			connection(ipadd,"run"+str(mr))
			#print("Wicket remaining",5-wicket)
			#print("You need ",x-totalrun+1,"to win")
				
		else:
			totalrun+=bowl
		ballcount+=1
		#print(ballcount)
		if(ballcount%6==0):
			mb=ballcount//6
			mr=totalrun
			mw=wicket
			print("end of over",ballcount//6)
			print( "totalruns",totalrun,"wickets lost",wicket)
			connection(ipadd,"wicket"+str(mw))
			connection(ipadd,"run"+str(mr))
			connection(ipadd,"Overs"+str(mb))
		
		if(totalrun==x):
			print("Scores level")
			connection(ipadd,"scores level")
			print("Wickets remaining",5-wicket)
			connection(ipadd,"wickets remaining"+str(5-wicket))
		if(totalrun>x):
			print("YOU LOST")
			connection(ipadd,"YOU WON")
			return 1
	

	print("YOU WON")
	connection(ipadd,"YOU LOST")
	return 0
	
	
		












	
	

def receive():
	
	servername='127.0.0.1'
	serverport=1200
	clientsocket=socket(AF_INET,SOCK_STREAM)
	clientsocket.connect((servername,serverport))
	#connection.socket
	x=clientsocket.recv(1224)
	x=x.decode('utf8')
	#print(int(x))
	clientsocket.close()
	return int(x)
	





def runcheck(x):

	if(x>6 or x<1):
		return 0
	return 1


def battingsecond(x):
	totalrun=0
	wicket=0
	ballcount=0
	while(ballcount!=12 and wicket!=5):
		bat=int(input())
		while(runcheck(bat)==0):
			print("invalid run")
			bat=int(input())
		bowl=receive()
		if(bat==bowl):
			print("OUT")
			wicket+=1
			if(wicket==5):
				print("YOU LOST")
				return 0
			print("Wicket remaining",5-wicket)
			print("You need ",x-totalrun+1,"to win")		
		else:
			totalrun+=bat
		ballcount+=1
		#print(ballcount)
		if(ballcount%6==0):
			print("end of over",ballcount//6)
			print("You need ",x-totalrun+1,"to win")	
			print("Wickets remaining",5-wicket)
		
		if(totalrun==x):
			print("Scores level")
			print("Wickets remaining",5-wicket)
		if(totalrun>x):
			print("YOU WON")
			return 1
	

	print("YOU LOST	")
	return 0
	




def bowlingfirst():
	totalrun=0
	wicket=0
	ballcount=0
	while(ballcount!=12 and wicket!=5):
		bat=int(input())
		while(runcheck(bat)==0):
			print("invalid run")
			bat=int(input())
			
		bowl=receive()
		if(bat==bowl):
			print("OUT")
			wicket+=1
			print("Wicket remaining",5-wicket)
			print("Runs scored by opponent",totalrun)
		else:
			totalrun+=bat
		ballcount+=1
		#print(ballcount)
		if(ballcount%6==0):
			print("end of over",ballcount//6)
			print( "Runs scored by opponent",totalrun,"wickets left",5-wicket)
	
	print(totalrun)
	return totalrun
	
		






def battingfirst():
	totalrun=0
	wicket=0
	ballcount=0
	while(ballcount!=12 and wicket!=5):
		bat=int(input())
		while(runcheck(bat)==0):
			print("invalid run")
			bat=int(input())
			
		bowl=receive()
		#print(bowl)
		if(bat==bowl):
			print("OUT")
			wicket+=1
			print("Wicket remaining",5-wicket)
			print("Runs scored",totalrun)
		else:
			totalrun+=bat
		ballcount+=1
		#print(ballcount)
		if(ballcount%6==0):
			print("end of over",ballcount//6)
			print( "totalruns",totalrun,"wickets lost",wicket)
	

	print(totalrun)
	
	return totalrun




def bowlingsecond(x):
	totalrun=0
	wicket=0
	ballcount=0
	while(ballcount!=12 and wicket!=5):
		bowl=int(input())
		while(runcheck(bowl)==0):
			print("Enter valid run")
			bowl=int(input())
		bat=receive()
		if(bat==bowl):
			print("OUT")
			wicket+=1
			print(5-wicket," wickets to win")
			print("runs needed by opponent to win",x-totalrun+1)
			if(wicket==5):
				print("YOU WON")
				return 1
		else:
			totalrun+=bat
			if(totalrun==x):
				print("Scores level")
			if(totalrun>x):
				print("Opponent won")
				return 0
		ballcount+=1
		if(ballcount%6==0):
			print("end of over",ballcount//6)
			print("You need",5-wicket,"wickets to win")
			print("runs needed by opponent to win",x-totalrun+1)
	
	print("YOU WON")
	return 1
				





import random
import math

print("select options")
print("enter 1 for single player")
print("enter 2 for multiplayer")

choice=int(input())
if(choice==1):
	#single player
	print("Choose your opton for toss")
	print(" enter 1 for heads")
	print(" enter 2 for tails")
	tosschoice=int(input())
	toss=random.randint(0,1) #coin
	if(toss==tosschoice):
		print("You won the toss")
		print(" enter 1 for batting")
		print(" enetr 2 for bowling")
		clientchoice=int(input())
		if(clientchoice==1):
			#batting
			userscore=battingfirst()
			print("End of innings")
			userbow=bowlingsecond(userscore)
		else:
			userbow=bowlingfirst()
			print("End of innings")
			userbat=battingsecond(userbow)
			
	else:
		
		
			
			
	

	
		print("You lost the toss")
		serverchoice=random.randint(0,1)
		if(serverchoice==1):
			print("Other player choose to bat")
			userbow=bowlingfirst()
			print("End of innings")
			userbat=battingsecond(userbow)
			

		else:
			
			print("Other player choose to bowl")
			userscore=battingfirst()
			print("End of innings")
			userbow=bowlingsecond(userscore)




else:
	
	print("enter your opponents ip address")
	ipadd=input()
	message="Enter your choice for toss  1.Head 2 Tail" 
	opponenttoss=connection(ipadd,message)
	toss=random.randint(1,2)
	if(toss==opponenttoss):
		print("YOU LOST THE TOSS")
		message="YOU WON THE TOSS  ENTER 1.BATTING  2.BOWLING"
		oppochoice=connection(ipadd,message)
		if(oppochoice==1):
			oppotarget=batting1st(ipadd)
			connection(ipadd,"Your innings ended")
			print("opponent innings ended")
			batting2nd(ipadd,oppotarget)
			

		else:
			metarget=batting2nd(ipadd)
			connection(ipadd,"opponents innings ended")
			print("Your innings ended")
			batting1st(ipadd,metarget)
			
			
	else:
		print("You Won the Toss")
		print("ENTER 1.BATTING  2.BOWLING")
		mychoice=int(input())
		if(mychoice==1):
			print("YOUR BATTING STARTS")
			connection(ipadd,"YOUR BOWLING STARTS")
			metarget=batting1st(ipadd)
			connection(ipadd,"opponents innings ended")
			print("Your innings ended")
			batting2nd(ipadd,metarget)
			
			
		
		else:
			oppotarget=batting2nd(ipadd)
			connection(ipadd,"Your innings ended")
			print("opponent innings ended")
			batting1st(ipadd,oppotarget)
			
	
