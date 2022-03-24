# sabemos que  z = h*y e y = = c*u
# então:
# 
# z = h*(c*u) 
#
# como a convolução é comutativa, temos:
#  z = (h*c)*u ; 
#
#  h*c = e1 aproximadamente; portanto temos :
#  
#  z = e1*u
#
# olhando para o processo de convolução, podemos tirar algumas propiedades:
#
#  k = 1 -> (e1)1.u1    ....
#  k = 2 -> (e1)1.u2    ....
#  k = 3 -> (e1)1.u3   ....
#  ....
#  Apresentando as primeira parcelas de cada k pertencente a z é facil perceber
#  que o somente os termos multiplicados por (e1)1 irão permanecer, pois este
#  é o único elemento de e1 que é igual a 1; 
#
#  portanto, qual será o último k onde (e1)1.uN (para um N qualquer) irá satis- 
#  fazer k + 1 = 1 + N ?; será para o maior valor de N possível; então N = K.
#
#    supondo que u tenha tamanho m e e1 tamanho n, a convolução será :
#  
#  k = 1 -> 1.u1
#  k = 2 -> 1.u2 + 0 + 0 ....
#  k = 3 - > 1.u3 + 0 + 0 ...
#  ....
#  k = m -> 1.um + 0 + 0 ....
#  ...
#  k = n + m - 1 -> 0.um 
#
#  Assim, os m primeiros elementos do vetor z serão o vetor u e os n-1 restantes
#  serão 0; pela notação matricia:
#  
#  z = [u 0], (u)m e (0)n-1
#
#  para finalizar, como e1 = h*c; e1 tem tamanho k + w - 1, supondo q h tenha
#  tamanho w e c tenha tamanho k.
#  
#  logo n = w + k - 1
#
#  entao a resposta final será z = [u 0], (u)m, (0)w+k-2  e (z)m+w+k-2
#  
#
# exemplo numérico:

import random as rand 
import numpy as np

e_1 = [1,0,0,0,0,0,0,0,0,0]

vet_aux  = [-1,1]
u = []
k =0
while (k < 50):
  u.append(rand.choice(vet_aux))
  k+=1
print(u, end ="\n\n")
z = np.convolve(e_1, u)

print(z)