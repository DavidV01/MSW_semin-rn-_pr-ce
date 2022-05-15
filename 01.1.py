import time
import numpy as np

#skalární součin 2 vektorů
t = time.time()

#zákl python
u=(2,3,5,9,8,5,6,2,4,4,8,5,3,1,2,58,8)
v=(2,6,1,58,5,3,8,4,6,8,4,3,2,5,1,2,3)
sk_soucin1=0

if len(u)==len(v):
  for i in range(len(u)):
    sk_soucin1+=u[i]*v[i]
else:
  raise Exception("jiná dimeze vektorů u a v")

print(sk_soucin1)

print(f"Čas v Pythonu: {time.time() - t} s")
print("\n")

t = time.time()

#numpy
v1=np.array([2,3,5,9,8,5,6,2,4,4,8,5,3,1,2,58,8])
v2=np.array([2,6,1,58,5,3,8,4,6,8,4,3,2,5,1,2,3])

sk_soucin2=v1 @ v2

print(sk_soucin2)

print(f"čas s modulem Numpy: {time.time() - t} s")