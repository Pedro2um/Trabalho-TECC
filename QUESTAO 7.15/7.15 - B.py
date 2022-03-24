
import random
import numpy as np
import matplotlib.pyplot as plt

def plus_minus_one_generator(): #funcao que retora +1 ou -1, com probabilidade 
  x = [-1,1,-1,1,-1,1]          # de 50% para ambos.
  return  random.choice(x)
  
def main():
  
  i =0
  u = []
  
  while(i < 50):
    u.append(plus_minus_one_generator()) ## constroi o u pedido
    i+=1
    
  print(u, end = "\n\n")
  
  plt.ion()
  plt.plot(u) ##plota u
  plt.show()
  
  c  = [1,0.7,-0.3]
  
  h = [0.9,-0.5,0.5,-0.4,0.3,-0.3,0.2,-0.1]
  
  y = np.convolve(c,u) ## y = c*u
  
  print(y, end = "\n\n")
  
  plt.ion()
  plt.plot(y) ##plota y
  plt.show()
  
  z = np.convolve(h,y) ## z = h*y
  
  print(z)

  plt.ion()
  plt.plot(z) ##plota z
  plt.show()
  plt.xlabel('U(azul), Y(verde) e Z(laranja)') # configurando as devidas 
                                                # legendas
  
  
  
  ##e1 = [1,0,0,0,0,0,0,0]                     #teste da propiedade e1*u = z,    
  ##u = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]  # aproximadamente
  ##print(np.convolve(e1,u))
    
  
  return
  
main()
