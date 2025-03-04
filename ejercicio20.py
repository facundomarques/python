'''
 Crea un programa que sume todos los números en una lista ingresada por el 
usuario

'''

# Programa para sumar todos los números en una lista

def sumar_numeros(lista):
    # Sumamos todos los números en la lista
    suma = sum(lista)
    return suma

# Solicitamos al usuario que ingrese una lista de números
numeros = input("Introduce una lista de números separados por espacios: ")

# Convertimos la entrada del usuario en una lista de números
numeros_lista = list(map(float, numeros.split()))

# Calculamos la suma de todos los números en la lista
suma_total = sumar_numeros(numeros_lista)

# Mostramos el resultado
print(f"La suma de todos los números en la lista es: {suma_total}")
