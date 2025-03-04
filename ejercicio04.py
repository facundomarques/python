'''  Ejercicio 4: Contador de Vocales
 Crea un programa que cuente el número de vocales en una palabra ingresada por el 
usuario


'''

def contar_vocales(palabra):
    vocales = 'aeiouAEIOU'
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador += 1
    return contador


palabra = input("Introduce una palabra: ")

numero_vocales = contar_vocales(palabra)
print(f"Número de vocales en la palabra es'{palabra}': {numero_vocales}")




