'''

Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo 
que 1 milla equivale a 1.60934 kilómetros



# Programa para convertir millas a kilómetros

def millas_a_kilometros(millas):
    # 1 milla equivale a 1.60934 kilómetros
    kilometros = millas * 1.60934
    return kilometros

# Solicitamos al usuario la distancia en millas
millas = float(input("Introduce la distancia en millas: "))

# Convertimos la distancia a kilómetros
kilometros = millas_a_kilometros(millas)

# Mostramos el resultado
print(f"{millas} millas equivalen a {kilometros} kilómetros")


'''
def millas_a_kilometros(millas):
  kilometros = millas * 1.60934
  return kilometros
millas = float(input("Introduce la distancia en millas: "))
kilometros = millas_a_kilometros(millas)
print(f"La distancia en kilometros es: {kilometros:.2f}")


