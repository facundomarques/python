'''
 Determinar el Día de la Semana
 Escribe un programa que determine el día de la semana correspondiente a un 
número ingresado por el usuario (1 para lunes, 2 para martes, etc.)

dias_semana = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
    7: "Domingo"
}


numero = int(input("Ingresa un número (1-7) para determinar el día de la semana: "))


if 1 <= numero <= 7:
    dia = dias_semana[numero]
    print(f"El número {numero} corresponde a {dia}.")
else:
    print("Por favor, ingresa un número válido entre 1 y 7.")
'''

def determinar_dia(numero):
  dias_semana = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
  if numero >= 1 and numero <= 7:
    return dias_semana[numero-1]
numero = int(input("Introduce un numero del 1 al 7: "))
nombre_dia = determinar_dia(numero)
print(f"El dia de la semana correspondiente es: {nombre_dia}")
  

