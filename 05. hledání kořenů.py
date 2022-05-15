#5. hledání kořenů
import math
import time
from scipy import optimize

#funkce
def f1(x):
  return x**3-x**2-x/4+1/4

def f2(x):
  return math.e**(x+x**2)-3

def f3(x):
  return 10*math.cos(2*math.pi*10*x+math.pi/2)

#výpočet kořenů funkcí
def f1_res(a,b,c,kroky):
  for i in range(kroky):  
    c=(a+b)/2  
    if (f1(a)*f1(c))<0:  #kořen někde mezi nima
      b=c
    else:
      a=c
  return c

def f2_res(a,b,c,kroky):
  for i in range(kroky):  
    c=(a+b)/2  
    if (f2(a)*f2(c))<0:  #kořen někde mezi nima
      b=c
    else:
      a=c
  return c

def f3_res(a,b,c,kroky):
  for i in range(kroky):  
    c=(a+b)/2  
    if (f3(a)*f3(c))<0:  #kořen někde mezi nima
      b=c
    else:
      a=c
  return c

t=time.time()
#uzavřená metoda, půlení intervalů

a=0     #od kam po kam zjišťuji kořeny
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

#Newtonova metoda
t=time.time()

a=0     #od kam po kam zjišťuji kořeny
b=1

koren1 = optimize.newton(f1, x0=(a+b/2))
koren2 = optimize.newton(f2, x0=(a+b/2))
koren3 = optimize.newton(f3, x0=(a+b/2))
print(f"kořen funkce f1= {koren1} -> Předpoklad x=1")
print(f"kořen funkce f1= {koren2} -> Předpoklad x=0,661")
print(f"kořen funkce f1= {koren3} -> Předpoklad x=0.05+k*0.05, dle a,b")


print(f"Čas pomocí Newtonovi metody: {time.time() - t} s\n")



