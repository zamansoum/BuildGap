
#   ____        _ _     _  _____             
#  |  _ \      (_) |   | |/ ____|            
#  | |_) |_   _ _| | __| | |  __  __ _ _ __  
#  |  _ <| | | | | |/ _` | | |_ |/ _` | '_ \ 
#  | |_) | |_| | | | (_| | |__| | (_| | |_) |
#  |____/ \__,_|_|_|\__,_|\_____|\__,_| .__/ 
#                                     | |    
#                                     |_|    
import sys
import apt
from termcolor import colored, cprint
import subprocess
from pathlib import Path
apt.apt_pkg.init()
cache=apt.Cache()
cache.open()
pkgname = str(sys.argv[1])

def wanchck():
	try:
		test=subprocess.call("ping -c 1" + " 9.9.9.9", shell=True, stdout=subprocess.DEVNULL)
		if test !=0:
			raise ValueError('No internet')
	except:
		print(colored("=>!Internet connection unavailable<=","red"))
		sys.exit()

#check if argument is provided and valid
def chckarg(pkgname=None):
	
	try:
		
		print(colored(pkgname,"cyan",attrs=["underline"]), colored(" package is selected","green"))
		
	except: 
		print(colored("=>!Missing package name!<=","red"))
		sys.exit()
	try:
		cache[pkgname]
		return pkgname

	except:
		print(colored("=>!This package does not exist!<=","red"))
		sys.exit()	

#Download the main package
def	getpkg():
	pkg=cache[pkgname]
	Path("/tmp/BuildGap").mkdir(parents=True, exist_ok=True)
	pkg.candidate.fetch_binary('/tmp/BuildGap/')


#Print Banner
print(colored(""" 
==================================
===|| BuildGap|| by zamansoum||===
==================================		
""", "yellow", attrs=["dark"]))

wanchck()
chckarg(pkgname)
getpkg()
#numdep=apt.Cache['apache2']
#print(numdep)
