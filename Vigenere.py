import os

#Realizado por la mamasita de María Serrano y el infiel de Sebas Contreras <3

alfabeto = "abcdefghijklmnñopqrstuvwxyz"
alphabet = alfabeto.upper()

letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))

#Código para cifrar el mensaje
def encrypt(message, key):
    encrypted = ""
    split_message = [
        message[i : i + len(key)] for i in range(0, len(message), len(key))
    ]

    for each_split in split_message:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] + letter_to_index[key[i]]) % len(alphabet) #C = (M+K)%27
            encrypted += index_to_letter[number]
            i += 1

    return encrypted

#Código para descifrar el mensaje
def decrypt(cipher, key):
    decrypted = ""
    split_encrypted = [
        cipher[i : i + len(key)] for i in range(0, len(cipher), len(key))
    ]

    for each_split in split_encrypted:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] - letter_to_index[key[i]]) % len(alphabet) #M = (C - K)%27
            decrypted += index_to_letter[number]
            i += 1

    return decrypted

def main():
  key = input("Introduce la llave del mensaje: ")
  key = key.upper()
  message = input("Introduce el mensaje: ")
  mensaje = message.replace(" ", "")
  mensaje_limpio = mensaje.upper()
    
  return mensaje_limpio, key

def opcionNum():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un número entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un número entero')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
 
    print ("1. Cifrar")
    print ("2. Descifrar")
    print ("3. Salir")
     
    print ("Elige una opcion")
    
    opcion = opcionNum()
    os.system("cls")

 
    if opcion == 1:
      os.system("cls")
      print('Cifrado')
      mensaje_limpio, key = main()
      encrypted_message = encrypt(mensaje_limpio, key)
      os.system("cls")
      print("Mensaje original: " + mensaje_limpio)
      print("Mensaje cifrado: " + encrypted_message)
      input("Presione Enter para continuar")
      os.system("cls")
    elif opcion == 2:
      os.system("cls")
      print('Descifrado')
      mensaje_limpio, key = main()
      decrypted_message = decrypt(mensaje_limpio, key)
      os.system("cls")
      print("Mensaje original: " + mensaje_limpio)
      print("Mensaje descifrado: " + decrypted_message)
      input("Presione Enter para continuar")
      os.system("cls")
    elif opcion == 3:
        salir = True
    else:
        print ("Introduce un número entre 1 y 3")
 
print ("Fin")