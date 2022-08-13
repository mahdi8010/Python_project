from colorama import  init , Fore
n=input('n=')
s=''
j=0
init() 
for i in n:
    if j%2==0:
        x=i.upper()    
        # s=s+x
        print(Fore.RED,x)        
    else:
        x=i.lower()
        # s=s+x
        print(Fore.BLUE,x)        
    j=j+1      
