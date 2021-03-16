import requests
import readline
from bs4 import BeautifulSoup

def rlinput(prefill):
   readline.set_startup_hook(lambda: readline.insert_text(prefill))
   try:
      return input()  # or raw_input in Python 2
   finally:
      readline.set_startup_hook()

query = ""

while True:
	query = rlinput(query)
	header = {'User-Agent':str(query)}
	r = requests.get("http://1.lab.sqli.site/getBrowserInfo.php",headers=header)

	soup = BeautifulSoup(r.text, "html.parser")
	print(r.text)
