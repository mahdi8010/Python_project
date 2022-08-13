from re import X
import numpy as np 
from numpy import pi
import sympy as sp
x,y=sp.symbols("x,y")
#f0=sp.Function("f")(x)
f1=x*sin(x) #int1
#print(sp.integrate(f,x)
print(f1.integrate((x)))
#g=sp.Function("g")(x,y)#ant 2 gane
#.evalf(5)#meghdar dehi

#x = sp.Symbol("x")
#print(sp.limit(sp.sin(x)/x, x, 0))#پیدا کردن حد توابع


#x = sp.Symbol("x")
#y = sp.Symbol("y")

#print(sp.solve(x ** 4 - 1, x))

#print(sp.solve([x + 5 * y - 2, -3 * x + 6 * y - 15], [x, y]))#حل معادلات

#x = sp.Symbol("x")
#f = sp.symbols("f", cls=sp.Function)

#o = sp.dsolve(f(x).diff(x, x) + f(x), f(x))
#print(o)

#x = sp.Symbol("x")
#y = sp.Symbol("y")
#print(sp.simplify((x + x * y) / x))#ساده سازی عبارات جبری
