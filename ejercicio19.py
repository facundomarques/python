'''

 Escribe un programa que determine si un año ingresado por el usuario es bisiesto o 
no.
'''

# Programa para determinar si un año es bisiesto

def es_bisiesto(ano):
    # Un año es bisiesto si es divisible por 4, pero no por 100,
    # a menos que también sea divisible por 400
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

# Solicitamos al usuario que ingrese un año
ano = int(input("Introduce un año: "))

# Determinamos si el año es bisiesto
if es_bisiesto(ano):
    print(f"El año {ano} es bisiesto.")
else:
    print(f"El año {ano} no es bisiesto.")
