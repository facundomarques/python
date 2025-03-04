'''
Crea un programa que verifique si una palabra ingresada por el usuario es un 
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).


def es_palindromo(palabra):
#se lleva a minusculas
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]

# Solicitar al usuario que ingrese una palabra
palabra = input("Introduce una palabra: ")

# Verificar y mostrar si la palabra es un palíndromo
if es_palindromo(palabra):
    print(f"La palabra '{palabra}' es un palíndromo.")
else:
    print(f"La palabra '{palabra}' no es un palíndromo.")

    
'''
def es_palindromo(palabra):
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
      return True
    else:
      return False
palabra = input("Introduce una palabra: ")

if es_palindromo(palabra):
    print("Es un palindromo!")
else:
    print("No es un palindromo!")
