#3. úvod do lingerby
import time
import matplotlib.pyplot as plt
import numpy as np
#přímá metoda řešení

x1=[]
y1=[]
x2=[]
y2=[]
for i in range(2,100):        #dokud něco tohle pojede a bude zvětšovat matici/znovu generovat s dimenzí +1    

  A = np.random.randint(1,500,size=(i,i))
  
  b = np.random.randint(1,500,size=(i))

  t=time.time()
  x = np.linalg.solve(A, b)  
  
  x1.append(i)  
  y1.append(time.time()-t)
  
  t=time.time()

  def jacobi(A, b, niteraci, x0=np.ones(len(A))):
      x = x0      
      D = np.diag(A)
      L = np.tril(A, k = -1)
      U = np.triu(A, k = 1)      
      for i in range(niteraci):
          x = (b - np.matmul((L + U),x))/D            
      return x

  x = jacobi(A, b, 10)
   
  x2.append(i)
  y2.append(time.time()-t)


plt.plot(x1, y1,label="přímá iterpolace")
plt.plot(x2, y2,label="Jacobiho interpolace")
plt.legend(loc='upper right')
plt.show()