import numpy as np
import math

def gcdExtended(a, b): 

    if a == 0 :  
        return b,0,1
             
    gcd,x1,y1 = gcdExtended(b%a, a) 

    x = y1 - (b//a) * x1 
    y = x1 
     
    return gcd,x,y

def matrix_cofactor(matrix):
    return np.linalg.inv(matrix).T * np.linalg.det(matrix)

def hill(opt, m, k, alfabeto, n):
    m = m.replace(' ', '')
    m = m.upper()
    letrasMensaje = list(m)
    j = 0
    matriz = np.zeros((2, math.ceil(len(letrasMensaje)/2)))
    for i in range(math.ceil(len(letrasMensaje)/2)):
        if(len(letrasMensaje)%2 == 0):
            matriz[0][i] = alfabeto.index(letrasMensaje[j])
            matriz[1][i] = alfabeto.index(letrasMensaje[j+1])
        if(len(letrasMensaje)%2 == 1):  
            if(len(letrasMensaje)>j+1):
                matriz[0][i] = alfabeto.index(letrasMensaje[j])
                matriz[1][i] = alfabeto.index(letrasMensaje[j+1])
            else:
                matriz[0][i] = alfabeto.index(letrasMensaje[j])
                matriz[1][i] = alfabeto.index('X')
        j = j+2     
   
    if(opt==0):
        adj = matrix_cofactor(k).T % n
        det = np.linalg.det(k) % n
        detinv = gcdExtended(int(det),n)[1]
        k = adj*detinv%27

    multiplica = np.dot(k,matriz)
    mod = multiplica % n

    return(mod)

m = 'KPTMWÑUQ'
k = [[5, 11], [8, 15]]
alpha = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
alfabeto = list(alpha)
mod = hill(0, m, k, alfabeto, 27)
palabra_final = []
for j in range(int(len(m)/2)):
    for i in range(2):
        palabra_final.append(alfabeto[int(mod[i][j])])

palabra_final = "".join(palabra_final)

print(palabra_final)