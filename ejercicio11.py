'''
 Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad 
actual


from datetime import datetime

año_actual = datetime.now().year

año_nacimiento = int(input("Ingresa tu año de nacimiento: "))


edad = año_actual - año_nacimiento

print(f"Tu edad actual es: {edad} años.")

'''

def calculadora_de_edad(anio_nacimiento):
  anio_actual = 2025
  edad = anio_actual - anio_nacimiento
  return edad

anio_nacimiento = int(input("Introduce tu año de nacimiento: "))
edad = calculadora_de_edad(anio_nacimiento)
print(f"Tienes {edad} años. ")
