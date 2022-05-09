#určitý integrál
import time
import math
import scipy.integrate as integrate

t = time.time()
fce="sin(x)"
#rozpětí od a do b a velikost obdélníku
a1=0
b=math.pi
obdelnik=10**6  #rozdělíme na obdelniky

n_casti=(abs(a1-b))/obdelnik #rozdělíme na n stejných částí
integral=0
a2=a1
for i in range(0,obdelnik):  
  integral+=math.sin(a2)*n_casti    #funkční hodnota fce*velikost jedné části
  a2=a2+n_casti 

print(f"Integrál od {a1} do {b} funkce {fce} = {integral}")    #a1 a2 rozděleny jen kvůli výslednému printu
print(f"Čas v Pythonu: {time.time() - t} s") 
print("\n")

#dle scipy
t = time.time()
fce="sin(x)"
a=0
b=math.pi
integral=0

integral = integrate.quad(lambda x: math.sin(x), a, b)
print(f"Integrál od {a} do {b} funkce {fce} = {integral[0]}") #[0] protože quad vrací 2 hodnoty, my chceme tu první
print(f"čas s modulem Scipy: {time.time() - t} s")
