'''
Crea un programa que cuente la cantidad de palabras en una oración ingresada por 
el usuario.




# Programa para contar la cantidad de palabras en una oración

def contar_palabras(oracion):
    # Dividimos la oración en palabras usando el método split()
    palabras = oracion.split()
    # Contamos la cantidad de palabras
    cantidad_palabras = len(palabras)
    return cantidad_palabras

# Solicitamos al usuario que ingrese una oración
oracion = input("Introduce una oración: ")

# Contamos las palabras en la oración
cantidad_palabras = contar_palabras(oracion)

# Mostramos el resultado
print(f"La cantidad de palabras en la oración es: {cantidad_palabras}")

'''
def contar_palabras(frase):
  palabras = frase.split()
  cantidad_palabras = len(palabras)
  return cantidad_palabras
oracion = input("introduce una oracion: ")
numero_palabras= contar_palabras(oracion)
print(f"Laoracion tiene {numero_palabras} palabras")

