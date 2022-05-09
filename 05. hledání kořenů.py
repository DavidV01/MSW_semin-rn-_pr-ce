#5. hledání kořenů
import time
import math


t=time.time()
#uzavřená metoda, půlení intervalů
#funkce
def f1(x):
  return x**3-x**2-x/4+1/4

def f2(x):
  return math.e**(x+x**2)-3

def f3(x):
  return 10*math.cos(2*math.pi*10*x+math.pi/2)

#výpočet kořenů funkcí
def f1_res(a,b,c,kroky):
  for i in range(poc_kroku):  
    c=(a+b)/2  
    if (f1(a)*f1(c))<0:  #kořen někde mezi nima
      b=c
    else:
      a=c
  return c

def f2_res(a,b,c,kroky):
  for i in range(poc_kroku):  
    c=(a+b)/2  
    if (f2(a)*f2(c))<0:  #kořen někde mezi nima
      b=c
    else:
      a=c
  return c

def f3_res(a,b,c,kroky):
  for i in range(poc_kroku):  
    c=(a+b)/2  
    if (f3(a)*f3(c))<0:  #kořen někde mezi nima
      b=c
    else:
      a=c
  return c

#"main"
a=0
b=1
c=0
poc_kroku=50  

koren_f1=f1_res(a,b,c,poc_kroku)
koren_f2=f2_res(a,b,c,poc_kroku)
koren_f3=f3_res(a,b,c,poc_kroku)

print(f"kořen funkce f1= {koren_f1} -> Předpoklad x=1")
print(f"kořen funkce f2= {koren_f2} -> Předpoklad x=0,661")
print(f"kořen funkce f3= {koren_f3} -> Předpoklad x=0.05+k*0.05, dle a,b")
print(f"Čas pomocí metody Bisekce: {time.time() - t} s\n")

#Bernoulliho metoda, pro exp. fce pouze
t=time.time()
def Bernoulli(n,seznam,m,a0):    #vycházím z algoritmu na webowých stránkách: http://physics.ujep.cz/~jskvor/NME/DalsiSkripta/numerickemetody.pdf, str.90  #jen pro polynomiální fce
  y=[]
  yk=0
  alpha=[]

  for i in range(n):
    if i!=n-1:
      y.append(0)
    else:
      y.append(1)
  
  for k in range(n+1,m):    
    yk=0

    for j in range(len(seznam)):           
      yk+=seznam[j]*y[len(y)-1-j] 

    y.append(yk)
    alpha.append(y[-1]/y[-2])

  return yk,alpha

fce="x**3-x**2-x/4+1/4"   #vše z této fce přepíšu do proměnných
n=3
seznam=[1,1/4,-1/4]
iterace=20
yk,alpha=Bernoulli(n,seznam,iterace,1)

print(f"koren = {alpha[-1]}")

print(f"Čas pomocí Bernoulliho metody: {time.time() - t} s\n")
