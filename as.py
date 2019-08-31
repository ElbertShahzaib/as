import requests

headers = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"
}
cor = ['\033[95m', '\033[96m', '\033[92m','\033[93m','\033[91m','\033[0m'] #

print  """
        
          ========  ========  =========  ======      = ========  = ======
          =         =     ==      =      =      ]    =           =      =
          =         =     ==      =      =       ]   =           =      =
          ========  ========      =      =        ]  = =======   = ======
                 =  =             =      =       ]   =           =  \ \
                           =  =             =      =      ]    =           =   \ \
                   ========  =         =========  ======      = ========  =    \  """
print "                "
print "                "

print "[!] It is in your own risk !!!"
print "                "
print "[+] If google adsense Detect This Trafic Then You Are Banned From Google " 
print "                "

site = raw_input("[>]Enter your Blog Address : ")
blog = input("[>]Enter The number of Viewers : ")

def run():
	url = requests.get(site, headers=headers)
	url.content
	print "["+str(i)+"]" + "[+] SuccessFully View Blog"


if __name__ == '__main__':
	for i in range(blog):
		run()
    
			
