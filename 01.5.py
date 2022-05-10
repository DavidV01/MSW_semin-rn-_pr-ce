#Transpozice matice
import numpy as np
import time
t = time.time()

A=[[0,1,2,3],[4,5,6,7]]
B = [[0 for i in range(len(A))] for j in range(len(A[0]))]    #A[0] proto, abych udělal matici transponovanou -> 2širokou, 4 na výšku


for i in range(len(A)):
  for j in range(len(A[i])):
    B[j][i]=A[i][j]

print(f"Matice A: ")
for i in range(len(A)):
  print(A[i])

print("\n")

print(f"Matice transponovaná: ")
for i in range(len(B)):
  print(B[i])

print(f"Čas v Pythonu: {time.time() - t} s")

print("\n")

#numpy
t=time.time()
A=np.array([[0,1,2,3],[4,5,6,7]])
print(f"Matice A: \n {A} \n")
print(f"Transponovaná matice: \n {A.T}")

print(f"Čas v Numpy: {time.time() - t} s")

