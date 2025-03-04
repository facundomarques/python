'''
Calculadora de Descuento
 Crea un programa que calcule el precio final de un artículo después de aplicar un 
descuento del 20%.


'''

def calculo_total(precio):
  descuento = precio * 0.20
  total = precio - descuento
  return total

precio_original = float(input("Introduzca el precio del articulo: "))

precio_descuento = calculo_total(precio_original)


print(f"El total a pagar, incluyendo descuento 20%, es: {precio_descuento}")
