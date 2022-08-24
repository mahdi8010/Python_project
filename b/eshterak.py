
#eshterak bin do list 
#1,one tedad list  barabar
A=list(input('A?'))

B=list(input('B?'))

c1=int(len(A))
print(f'A {c1} mgmoe dard')
c2=int(len(B))
print(f'B {c2} mgmoe dard')
d1= range(c1)
d2=range(c2)
if d1==d2:

  for i in d1 : 
     if A[i]==B[i] :
      print(f'{A[i]}=={ B[i]}')
     else :
       print(f'{A[i]}!={ B[i]}')

#2,two tedad list na barabar 
elif d1!=d2 :
  if c1>c2 :
    for i in d2 : 
     if A[i]==B[i] :
      print(f'{A[i]}=={ B[i]}')
     else :
       print(f'{A[i]}!={ B[i]}')
    z=c1-c2
    for i in range(z):
     v=A[-(i+1)]
     print(f'shomare {-(i+1)} ==> {v}' )

  else :
    for i in d1 : 
     if A[i]==B[i] :
      print(f'{A[i]}=={ B[i]}')
     else :
       print(f'{A[i]}!={ B[i]}')
    z=c2-c1
    for i in range(z):
     v=B[-(i+1)]
     print(f'shomare {-(i+1)} ==> {v}' )

else :
   print('error')

