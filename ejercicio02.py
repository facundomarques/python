'''

Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo 
una propina del 15% sobre el total de la cuenta

'''



def calculo_total(cuenta):
  propina = cuenta * 0.15
  total = cuenta + propina
  return total

cuenta = float(input("Ingrese el total de la cuenta: "))

total_a_pagar = calculo_total(cuenta)


print(f"El total a pagar, incluyendo una propina del 15%, es: {total_a_pagar}")
