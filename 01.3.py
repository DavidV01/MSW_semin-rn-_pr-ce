#součet 2 stejných matic
import time
import numpy as np

t = time.time()

A=[[1,2,3],[2,5,6],[3,2,5]]
B=[[68,23,3],[2,4,3],[1,5,67]]

for i in range(len(A)):  
  for j in range(len(A[i])):
    A[i][j]=A[i][j]+B[i][j]

#výpis matice
for i in range(len(A)):
  print(A[i])

print(f"Čas v Pythonu: {time.time() - t} s")

print("\n")

#numpy
t = time.time()

A=np.array([[1,2,3],[2,5,6],[3,2,5]])
B=np.array([[68,23,3],[2,4,3],[1,5,67]])

print(A+B)

print(f"čas s modulem Numpy: {time.time() - t} s") 