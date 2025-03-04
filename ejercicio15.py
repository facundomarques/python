'''
Escribe un programa que convierta un número de minutos en horas y minutos. Por 
ejemplo, 145 minutos serían 2 horas y 25 minutos




def convertir_minutos(minutos_totales):
    horas = minutos_totales // 60
    minutos = minutos_totales % 60
    return horas, minutos

minutos_totales = int(input("Ingresa el número de minutos: "))

horas, minutos = convertir_minutos(minutos_totales)

print(f"{minutos_totales} minutos son equivalentes a {horas} horas y {minutos} minutos.")
'''

def convertir_a_horas_y_minutos(minutos):
  horas = minutos // 60
  minutos_restantes = minutos % 60
  return horas, minutos_restantes

minutos = int(input("Introduce la cantidad de minutos: "))
horas, minutos_restantes = convertir_a_horas_y_minutos(minutos)

print(f"{minutos} serian {horas} horas y {minutos_restantes} minutos")
