import os
import sys
import time
import requests
from datetime import datetime

red = "\033[0;31m"
white = "\033[0m"
blue = "\033[94m"
green = "\033[92m"
magenta = "\033[1;35;40m"

tag3 = red+"[X] "+white
tag2 = green+"[+] "+white
tag1 = red+"[+] "+white
tag = blue+"[*] "+white

mBanner = """  

██████╗ ███████╗██████╗ ███████╗ █████╗ ████████╗ 
██╔══██╗██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝
██████╔╝█████╗  ██████╔╝█████╗  ███████║   ██║   
██╔══██╗██╔══╝  ██╔═══╝ ██╔══╝  ██╔══██║   ██║   
██║  ██║███████╗██║     ███████╗██║  ██║   ██║   
╚═╝  ╚═╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   

@DyonisoHacks
-> Select only options:
""" 

banner2 = blue+"""
  ,.,,,,,,,,,,,.,,,,,,,,
    . .. .  . / ..  .
           , /
         , '/
        , '/
       , '/ _____,
     .'____, '
           /, '
          /, '
         /, '
        / '   
              -> Repeater >.<
"""

os.system("cls")

def collectData():
	headers = []
	links = []
	data = []

	print("")
	print(tag2+"Geting headers...")
	rawHeaters = open('data/headers.txt').read();
	headers = rawHeaters.rsplit("++");

	print(tag2+"Geting links...")
	rawLink = open('data/links.txt').read();
	links = rawLink.rsplit("++");

	print(tag2+"Geting data...")
	rawData = open('data/data.txt').read();
	data = rawData.rsplit("++");

	print("")
	print(tag2+"Complete!")
	attack(links, headers, data)

def attack(links, headers, data):
	for link in links:
		print(tag+"Target: "+link.strip())
	
	print("")
	strCount = input(tag+"Type count time > ")	
	srtDelay = input(tag+"Choose delay > ")	
	rInput = input(tag+"Type yes to start > ")

	delay = 1
	count = 5
	try:
		delay = int(srtDelay)
		count = int(strCount)

	except Exception as e:
		pass
	
	if rInput == "yes" or rInput == "y":
		print(banner2)
		print(tag+"Starting...")
		time.sleep(3)

		while True:
			if count < 1:
				print("")
				print(tag3+"Finished at "+datetime.today().strftime('%Y-%m-%d'))
				break
			count = count - 1

			for rawheader in headers:
				for link in links:
					for dt in data:
						url = link.strip()
						hearder = {}
						try:
							print("")
							print(tag2+"Using header type 1")
							hearder = {
							"Host" : rawheader.rsplit(": ")[1].split("\n")[0],
							"Connection" : rawheader.rsplit(": ")[2].split("\n")[0],
							"Content-Length" : rawheader.rsplit(": ")[3].split("\n")[0],
							"Cache-Control" : rawheader.rsplit(": ")[4].split("\n")[0],
							"Upgrade-Insecure-Requests" : rawheader.rsplit(": ")[5].split("\n")[0],
							"Origin" : rawheader.rsplit(": ")[6].split("\n")[0],
							"Content-Type" : rawheader.rsplit(": ")[7].split("\n")[0],
							"User-Agent" : rawheader.rsplit(": ")[8].split("\n")[0],
							"Accept" : rawheader.rsplit(": ")[9].split("\n")[0],
							"Sec-Fetch-Site" : rawheader.rsplit(": ")[10].split("\n")[0],
							"Sec-Fetch-Mode" : rawheader.rsplit(": ")[11].split("\n")[0],
							"Sec-Fetch-User" : rawheader.rsplit(": ")[12].split("\n")[0],
							"Sec-Fetch-Dest" : rawheader.rsplit(": ")[13].split("\n")[0],
							"Referer" : rawheader.rsplit(": ")[14].split("\n")[0],
							"Accept-Encoding" : rawheader.rsplit(": ")[15].split("\n")[0],
							"Accept-Language" : rawheader.rsplit(": ")[16].split("\n")[0],
							"Cookie" : rawheader.rsplit(": ")[17].split("\n")[0]
						}	
						except Exception as e:
							print(tag2+"Using header type 2")
							hearder = {
								"Host" : rawheader.rsplit(": ")[1].split("\n")[0],
								"Content-Length" : rawheader.rsplit(": ")[2].split("\n")[0],
								"Cache-Control" : rawheader.rsplit(": ")[3].split("\n")[0],
								"Upgrade-Insecure-Requests" : rawheader.rsplit(": ")[4].split("\n")[0],
								"Origin" : rawheader.rsplit(": ")[5].split("\n")[0],
								"Content-Type" : rawheader.rsplit(": ")[6].split("\n")[0],
								"User-Agent" : rawheader.rsplit(": ")[7].split("\n")[0],
								"Accept" : rawheader.rsplit(": ")[8].split("\n")[0],
								"Referer" : rawheader.rsplit(": ")[9].split("\n")[0],
								"Accept-Encoding" : rawheader.rsplit(": ")[10].split("\n")[0],
								"Accept-Language" : rawheader.rsplit(": ")[11].split("\n")[0],
								"Cookie" : rawheader.rsplit(": ")[12].split("\n")[0],
								"Connection" : rawheader.rsplit(": ")[13].split("\n")[0]
						}

						print("")
						print(tag2+"Sending to target "+link)
						print(tag+"Header: "+str(hearder))
						print(tag+"Data: "+dt)
						print(tag+"Method POST")

						try:
							r = requests.post(url, headers=hearder, data=dt)
							print("")
							print(tag+"Content: "+str(r.content))
							print(tag+"Code: "+str(r.status_code))
							time.sleep(delay)

						except Exception as e:
							print(tag3+"Error to connect in "+url)
					

def fast():
	print("")
	print(tag2+"Geting headers...")
	wHeaders = open('data/headers.txt').read();
	rawheader = wHeaders.rsplit("++");

	print(tag2+"Geting links...")
	rawLink = open('data/links.txt').read();
	links = rawLink.rsplit("++");

	print(tag2+"Geting data...")
	rawData = open('data/data.txt').read();
	data = rawData.rsplit("++");

	print(banner2)
	print(tag+"Starting...")
	time.sleep(1)

	url = links[0].strip()

	hearder = {}
	try:
		print("")
		print(tag2+"Using header type 1")
		hearder = {
		"Host" : rawheader[0].rsplit(": ")[1].split("\n")[0],
		"Connection" : rawheader[0].rsplit(": ")[2].split("\n")[0],
		"Content-Length" : rawheader[0].rsplit(": ")[3].split("\n")[0],
		"Cache-Control" : rawheader[0].rsplit(": ")[4].split("\n")[0],
		"Upgrade-Insecure-Requests" : rawheader[0].rsplit(": ")[5].split("\n")[0],
		"Origin" : rawheader[0].rsplit(": ")[6].split("\n")[0],
		"Content-Type" : rawheader[0].rsplit(": ")[7].split("\n")[0],
		"User-Agent" : rawheader[0].rsplit(": ")[8].split("\n")[0],
		"Accept" : rawheader[0].rsplit(": ")[9].split("\n")[0],
		"Sec-Fetch-Site" : rawheader[0].rsplit(": ")[10].split("\n")[0],
		"Sec-Fetch-Mode" : rawheader[0].rsplit(": ")[11].split("\n")[0],
		"Sec-Fetch-User" : rawheader[0].rsplit(": ")[12].split("\n")[0],
		"Sec-Fetch-Dest" : rawheader[0].rsplit(": ")[13].split("\n")[0],
		"Referer" : rawheader[0].rsplit(": ")[14].split("\n")[0],
		"Accept-Encoding" : rawheader[0].rsplit(": ")[15].split("\n")[0],
		"Accept-Language" : rawheader[0].rsplit(": ")[16].split("\n")[0],
		"Cookie" : rawheader[0].rsplit(": ")[17].split("\n")[0]
	}	
	except Exception as e:
		print(tag2+"Using header type 2")
		hearder = {
			"Host" : rawheader[0].rsplit(": ")[1].split("\n")[0],
			"Content-Length" : rawheader[0].rsplit(": ")[2].split("\n")[0],
			"Cache-Control" : rawheader[0].rsplit(": ")[3].split("\n")[0],
			"Upgrade-Insecure-Requests" : rawheader[0].rsplit(": ")[4].split("\n")[0],
			"Origin" : rawheader[0].rsplit(": ")[5].split("\n")[0],
			"Content-Type" : rawheader[0].rsplit(": ")[6].split("\n")[0],
			"User-Agent" : rawheader[0].rsplit(": ")[7].split("\n")[0],
			"Accept" : rawheader[0].rsplit(": ")[8].split("\n")[0],
			"Referer" : rawheader[0].rsplit(": ")[9].split("\n")[0],
			"Accept-Encoding" : rawheader[0].rsplit(": ")[10].split("\n")[0],
			"Accept-Language" : rawheader[0].rsplit(": ")[11].split("\n")[0],
			"Cookie" : rawheader[0].rsplit(": ")[12].split("\n")[0],
			"Connection" : rawheader[0].rsplit(": ")[13].split("\n")[0]
	}

	print("")
	print(tag2+"Sending to target "+url)
	print(tag+"Header: "+str(hearder))
	print(tag+"Data: "+data[0].strip())
	print(tag+"Method POST")

	try:
		r = requests.post(url, headers=hearder, data=data[0].strip())
		print("")
		print(tag+"Content: "+str(r.content))
		print(tag+"Code: "+str(r.status_code))

	except Exception as e:
		print(tag3+"Error to connect in "+url)

	print("")
	print(tag3+"Finished at "+datetime.today().strftime('%Y-%m-%d'))

  
def banner():
	print(mBanner) 