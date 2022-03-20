x=int(input('meghdar aval : '))
y=int(input('meghdar akhar : '))
z=range(x,y+1)


print('----------------------------')
for b in z:
    v=int(((b+1)*b)/2)
    if v % b==0 :
       if v % b==0 :
         m=int(v/b)
         print( f'moraba gami: {b}-->> {b} * {m} --> {v}')
    