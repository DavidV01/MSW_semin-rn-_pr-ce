#využil jsem kodu ze cvičení 1
#určitý integrál
import time
import math
import scipy.integrate as integrate

#3 funkce
def f1(a,vel_casti,n_casti):       #f1 = x**3- 3*x + 2
  integ=0  

  for i in range(0,vel_casti):  
    integ+=(a**3- 3*a + 2)*n_casti    #funkční hodnota fce*velikost jedné části
    a=a+n_casti
  return integ

def f2(a,vel_casti,n_casti):    #f2=e**x
  integ=0

  for i in range(0,vel_casti):  
    integ+=(math.e**(a)-10)*n_casti    #funkční hodnota fce*velikost jedné části
    a=a+n_casti
  return integ

def f3(a,vel_casti,n_casti):     #f3 = (math.log(x-20)+10))
  integ=0

  for i in range(0,vel_casti):  
    integ+=(math.log(a**2+5)+10)*n_casti    #funkční hodnota fce*velikost jedné části
    a=a+n_casti
  return integ

#pomocí pythonu a Math
t = time.time()
#rozpětí od a do b a velikost obdélníku
a1=1
b=10
obdelnik=10**6  #rozdělíme na obdelniky

n_casti=(abs(a1-b))/obdelnik #rozdělíme na n stejných částí

integral1=f1(a1,obdelnik,n_casti)
integral2=f2(a1,obdelnik,n_casti)
integral3=f3(a1,obdelnik,n_casti)


print(f"Integrál od {a1} do {b} funkce f1 = {integral1}")    
print(f"Integrál od {a1} do {b} funkce f2 = {integral2}")
print(f"Integrál od {a1} do {b} funkce f3 = {integral3}")
print(f"Čas v Pythonu: {time.time() - t} s\n") 

#pomocí scipy
t = time.time()
integral1_scipy = integrate.quad(lambda x: x**3- 3*x + 2, a1, b)
integral2_scipy = integrate.quad(lambda x: math.e**(x)-10, a1, b)
integral3_scipy = integrate.quad(lambda x: (math.log(x**2+5)+10), a1, b)

print(f"Integrál od {a1} do {b} funkce f1 = {integral1_scipy[0]}")    
print(f"Integrál od {a1} do {b} funkce f2 = {integral2_scipy[0]}")
print(f"Integrál od {a1} do {b} funkce f3 = {integral3_scipy[0]}")
print(f"Čas v knihovně Scipy: {time.time() - t} s") 