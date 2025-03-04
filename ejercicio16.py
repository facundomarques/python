'''
Ejercicio 16: Contador de Números Pares e Impares
 Crea un programa que cuente y muestre la cantidad de números pares e impares en 
una lista ingresada por el usuario.


# Función para contar números pares e impares
def contar_pares_impares(lista_numeros):
    cantidad_pares = 0
    cantidad_impares = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            cantidad_pares += 1
        else:
            cantidad_impares += 1
    return cantidad_pares, cantidad_impares

# Solicitar al usuario que ingrese la lista de números
entrada = input("Ingresa una lista de números separados por espacios: ")
lista_numeros = list(map(int, entrada.split()))

# Contar los números pares e impares
pares, impares = contar_pares_impares(lista_numeros)

# Mostrar el resultado
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")

'''
def contar_pares_impares(lista):
    pares = 0
    impares = 0
    for num in lista:
        if num % 2 == 0:
                pares = pares + 1
        else:
                impares + 1
    return pares, impares

numeros = list(map(int, input("Introduce una lista de numeros separados por espacios: ").split()))
pares, impares = contar_pares_impares(numeros)
print(f"Lalista contiene {pares} numeros pares y {impares} numeros impares")



