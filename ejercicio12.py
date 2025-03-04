'''
 Calculadora de Área de un Rectángulo
 Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la 
longitud y el ancho del rectángulo.

'''

# Función para calcular el área de un rectángulo
# Función para calcular el área de un rectángulo
def calcular_area_rectangulo(longitud, ancho):
    area = longitud * ancho
    return area

longitud = float(input("Ingresa la longitud del rectángulo: "))
ancho = float(input("Ingresa el ancho del rectángulo: "))

area = calcular_area_rectangulo(longitud, ancho)

print(f"El área del rectángulo es: {area:.2f} unidades cuadradas.")
