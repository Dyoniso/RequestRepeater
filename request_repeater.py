import sys
import os
if sys.version_info.major < 3:
    print("Repeater supports only Python3. Run the application in Python3 environment.")
    exit(0)
from core.main import *

def main():
	try:
		banner()
		print("* Select [1] to start. ")
		print("* Select [2] to test target.")
		print("* Select [3] to intall modules. ")
		print("* Select [4] to exit. ")
		print("")
		rInput = input(tag+"repeater > ")
		if rInput == "1" or rInput == "01":
			collectData()

		if rInput == "2" or rInput == "02":
			fast()

		if rInput == "3" or rInput == "03":
			os.chdir('install/requests-2.24.0/')
			os.system('python setup.py')

		if rInput == "4" or rInput == "04":
			exit(0)

	except(KeyboardInterrupt, SystemExit):
		print(tag3+"Tool Interrupted"+"\n")
		exit(0)
		
if __name__ == "__main__":
	main()
	

