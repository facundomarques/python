'''

Verificación de Número Primo
 Escribe un programa que determine si un número ingresado por el usuario es primo 
o no



def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


numero = int(input("Ingresa un número para verificar si es primo: "))


if es_primo(numero):
    print(f"El número {numero} es primo.")
else:
    print(f"El número {numero} no es primo.")

'''
def es_primo(numero):
  if numero <=1:
    return False
  for i in range(2, numero):
    if numero % i == 0:
      return False
  return True
numero = int(input("introduce un numero: "))
if es_primo(numero):
  print(f"El numero {numero} es primo!")
else:
  print(f"El numero {numero} no es primo")



