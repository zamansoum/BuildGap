
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

apt.apt_pkg.init()
cache=apt.Cache()
cache.open()


#check if argument is provided and valid
def chckarg(pkgname=None):
	
	try:
		pkgname = str(sys.argv[1])
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

#Print Banner
print(colored(""" 
==================================
===|| BuildGap|| by zamansoum||===
==================================		
""", "yellow", attrs=["dark"]))

pkgname=chckarg()
#numdep=apt.Cache['apache2']
#print(numdep)
