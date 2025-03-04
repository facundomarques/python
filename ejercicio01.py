'''
Ejercicio 1: Conversor de Temperatura
Escribe un programa que convierta una temperatura de grados Celsius a grados
Fahrenheit.
 F=(celcius * 9/5) +32
'''


def celsius_a_farenheit(celsius):
  return celsius * (9/5) + 32
t_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
t_farenheit = celsius_a_farenheit(t_celsius)
print(f"La temperatura en grados Fahrenheit es: {t_farenheit}")


