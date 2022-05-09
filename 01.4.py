#kvadratická rovnice ------------------------VYMYSLET 5. PŘÍKLAD
import time
import math
from sympy.solvers import solve
from sympy import Symbol
t = time.time()

a=1
b=-2
c=1

x=[]    #množina výsledků

D=b**2-4*a*c

if D>0:
  x.append((-b/(2*a))+math.sqrt(D))
  x.append((-b/(2*a))-math.sqrt(D))
  
elif D==0:
  x.append(-b/(2*a))
else:
  print("Kvadratická rovnice nemá řešení v R**2")

print(x)
print(f"čas v Pythonu: {time.time() - t} s")

#sympy
t = time.time()
x = Symbol('x')
print(solve(x**2-2*x+1,x))
print(f"Čas s modulem Sympy: {time.time() - t} s")