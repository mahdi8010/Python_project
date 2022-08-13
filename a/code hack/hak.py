import requests
from colorama import  Fore,init

init()

search =['search/','login/','admin/']

url= input("  Enter url : ")

for page in search:
    req = requests.get("https://"+url+"/"+page)
    if req.status_code == 200:
        print(Fore.GREEN+" [+] "+Fore.WHITE+" page Ok "+url+"/"+page)
    else:
        print(Fore.RED+" [-] "+Fore.WHITE+" page NO Ok "+url+"/"+page)
