import math

x=8
y=12
x1=[1,2,3,4,5]
x2=[0,0,5,0,0]

z=math.ceil(x) #به بینهایت + گرد میکند 
z0=math.floor(x)#به بینهایت  - گرد میکند 
z1=math.comb(4, 3) #???????
z2=math.copysign(x, y)# مثبت و منفی کردن اعداد
z3=math.fabs(x)# قدر مطلق x
z4=math.factorial(x)#فاکتوریال یا x!
z5=math.fsum(x1)#همون sum 
z6=math.gcd(*x2)#.....
z7=math.isclose(x, y, rel_tol=1e-09, abs_tol=0.0)#نزدیک به هم x,y با درست و غلط میگوید
z8=math.isfinite(x) #nan and &+- را تشخیص میدهد 
z9=math.isinf(x) #&+- را تشخیص میدهد 
z10=math.isqrt(9)#ریشه اصلی را به ما می دهد مثلا این 3
z11=math.lcm(*x1)#????????
z12=math.frexp(2)#x == m*2 ** e
z13=math.ldexp(x, y)#معکوس z12
z14=math.modf(x)#????????
z15=math.perm(6,2)#تابعی که از مضارب 6 دورقمی به ما می دهد 
z16=math.prod(x1)#اعداد لیست را ضرب می کند  
z17=math.remainder(x, y)#مفدار اختلاف باقی مانده را از باقی مانده صفر می دهد 
z18=math.trunc(x)#مقدار واقعی x
z19=math.ulp(x)#......???
z20=math.exp(3.8596)#e = 2.718281…
z21=math.log(10)#log(x)/log(base) and to base e
z22=math.log2(2)#log(x, 2)
z23=math.log(x,y)#log(x, y)
z24=math.log10(x)#log(x,10)
z25=math.pow(x, y)#x^y
z26=math.sqrt(x)#جزر با فرجه 2
z27=math.acos(x)    #بر حسب رادیان
z28=math.asin(x)    #بر حسب رادیان
z29=math.atan(x)    #بر حسب رادیان
z30=math.acotan()   #بر حسب رادیان
z31=math.atan2(y, x)#بر حسب رادیان
z32=math.cos(x)     #بر حسب درجه 
z33=math.sin(x)    #بر حسب درجه
z34=math.tan(x)    #بر حسب درجه
z35=math.cotan()   #بر حسب درجه
z36=math.dist(x,y) #???????
z37=math.degrees(x)  #از رادیان به درجه
z38=math.radians(x)  #از درجه به رادیان 
z39=math.acosh(x)    #بر حسب رادیان
z40=math.asinh(x)    #بر حسب رادیان
z41=math.atanh(x)    #بر حسب رادیان
z42=math.cosh(x)     #بر حسب درجه 
z43=math.sinh(x)     #بر حسب درجه 
z44=math.tanh(x)     #بر حسب درجه 
z45=math.erf(x)     #تابع خطا

print(z20)


