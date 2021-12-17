import math
import numpy as np
import string


alphabet = list(string.ascii_uppercase)
alphabet2 = alphabet[:]
n = 5
matriz = np.zeros((n,n), dtype= str)


def playfair(text, key):
    key = key.replace(' ', '')
    key = key.upper()
    key = list(key)
    lon_key = len(key)

    for i in range(n):
        for j in range(n):

            k = j + (i*5)
            
            if (lon_key <= k):
  
                if(k-lon_key >= alphabet.index('J')):
                    matriz [i][j] = alphabet[(k+1)-lon_key]
                else:
                    matriz [i][j] = alphabet[k-lon_key]
            
            else: 
                print()
                if(alphabet2.index(key[k]) == alphabet.index(key[k])):
                    matriz [i][j] = key[k]
                    index = alphabet2.index(key[k])
                    alphabet2.remove(key[k])
                    alphabet2.insert(index, '')
                
                print(alphabet2)
    
    print(matriz)


def convertplaintext (plaintext):

    plaintext = plaintext.replace(' ', '')
    plaintext = list(plaintext)

    for i in range(len(plaintext)):
        
        if(i %2 == 1):
            if(plaintext[i-1] == plaintext[i]):
                plaintext.insert(i, 'X')

                if(len(plaintext)%2 == 1):
                    plaintext.append('X')

    final_plaintext = []

    for i in range(len(plaintext)):

        if(i %2 == 1):
                final_plaintext.append(plaintext[i-1] + plaintext[i])
        else:
            continue
        


    return final_plaintext

texto = convertplaintext('WITH A LITTLE HELP FROM MY FRIENDS')

print(playfair(texto,'BEATLES'))