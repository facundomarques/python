''' Verificación de Edad
 Escribe un programa que solicite la edad de un usuario y determine si es mayor de 
edad (mayor o igual a 18 años) o no

otro forma
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("No eres mayor de edad.")


'''
def verificar_edad(edad):
  if edad >= 18:
    return "Eres mayor de edad"
  else:
    return "Eres menor de edad"
edad = int(input("introduce tu edad: "))
mensaje = verificar_edad(edad)
print(mensaje)

