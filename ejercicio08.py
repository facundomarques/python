'''
Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
 Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona




def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Solicitar al usuario que ingrese su peso en kilogramos
peso = float(input("Introduce tu peso en kilogramos: "))

# Solicitar al usuario que ingrese su altura en metros
altura = float(input("Introduce tu altura en metros: "))

# Calcular el IMC
imc = calcular_imc(peso, altura)

# Mostrar el resultado del IMC
print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")

# Clasificación del IMC según la OMS
if imc < 18.5:
    print("Clasificación: Bajo peso")
elif 18.5 <= imc < 24.9:
    print("Clasificación: Peso normal")
elif 25 <= imc < 29.9:
    print("Clasificación: Sobrepeso")
else:
    print("Clasificación: Obesidad")
'''
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("introduce tu peso en Kg: "))
altura = float(input("introduce tu altura en metros: "))

imc = calcular_imc(peso, altura)
print(f"Tu indice de masa corporal es: {imc:.2f}")
