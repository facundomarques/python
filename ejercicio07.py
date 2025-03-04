'''
Crea un programa que realice operaciones aritméticas simples (suma, resta, 
multiplicación, división) según la elección del usuario
'''

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero no permitida."

def operaciones_aritmeticas():
    print("Selecciona la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    eleccion = int(input("Introduce el número de la operación que deseas realizar (1/2/3/4): "))

    numero1 = float(input("Introduce el primer número: "))
    numero2 = float(input("Introduce el segundo número: "))

    if eleccion == 1:
        print(f"Resultado: {suma(numero1, numero2)}")
    elif eleccion == 2:
        print(f"Resultado: {resta(numero1, numero2)}")
    elif eleccion == 3:
        print(f"Resultado: {multiplicacion(numero1, numero2)}")
    elif eleccion == 4:
        print(f"Resultado: {division(numero1, numero2)}")
    else:
        print("Operación no válida.")

operaciones_aritmeticas()
