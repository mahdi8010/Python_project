
c=name= input("Please enter your name:   ")
j= len(c)
j = int(j)
i=j-1

print(c)

class color :

    RED=   '\033[91m'
    BLUE=  '\033[94m'
    YELLOW='\033[93m'
    CYNE=  '\033[96m'
    GREEN= '\033[92m'
    WHITE=  '\033[4m' 

    END='\033[0m'

if  i==1:
    print ( color.YELLOW+c[0].upper()+color.END+'\n' + color.CYNE+c[i]+color.END )
elif  i==2 :
 print ( color.YELLOW+c[0].upper()+color.END+'\n' + color.CYNE+c[1]+color.END +'\n'+color.GREEN+c[i].upper()+color.END)   
elif  i==3 :
    print ( color.YELLOW+c[0].upper()+color.END+'\n' + color.CYNE+c[1]+color.END +'\n'+color.GREEN+c[2].upper()+color.END+'\n'+
    color.WHITE+c[i]+color.END)
elif  i==4 :
    print ( color.YELLOW+c[0].upper()+color.END+'\n' + color.CYNE+c[1]+color.END +'\n'+color.GREEN+c[2].upper()+color.END+'\n'+
    color.WHITE+c[3]+color.END+ '\n' +color.RED+c[i]+color.END)
elif  i==5 :
    print ( color.YELLOW+c[0].upper()+color.END+'\n' + color.CYNE+c[1]+color.END +'\n'+color.GREEN+c[2].upper()+color.END+'\n'+
    color.WHITE+c[3]+color.END+ '\n'+color.RED+c[4]+color.END + '\n'+color.BLUE+c[i]+color.END)
elif  i==6 :
    print ( color.YELLOW+c[0].upper()+color.END+'\n' + color.CYNE+c[1]+color.END +'\n'+color.GREEN+c[2].upper()+color.END+'\n'+
    color.WHITE+c[3]+color.END+ '\n'+color.RED+c[4]+color.END + '\n'+color.BLUE+c[5]+color.END+'\n'+color.GREEN+c[i].upper()+color.END)  
elif  i==7 :
    print ( color.YELLOW+c[0].upper()+color.END+'\n' + color.CYNE+c[1]+color.END +'\n'+color.GREEN+c[2].upper()+color.END+'\n'+
    color.WHITE+c[3]+color.END+ '\n'+color.RED+c[4]+color.END + '\n'+color.BLUE+c[5]+color.END+'\n'+color.GREEN+c[6].upper()+color.END
    +'\n'+color.YELLOW+c[i]+color.END)

print(f"Thank you for your attention { name } !")


z="ali"
#print(c.upper())
#print(z.lower())
#print(z.title())
