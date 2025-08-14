#funciones
def sumar(numero_uno, numero_dos):
    resultado_suma = numero_uno + numero_dos
    if(isinstance(numero_uno, int) and isinstance(numero_dos, int)):
     return f"la suma de los dos numeros es: {resultado_suma}"
    return "Solo se permiten numeros enteros"
print(sumar("hl","lol"))

def restar(numero_uno, numero_dos):
   resultado_resta = numero_uno - numero_dos
   if(isinstance(numero_uno, int) and isinstance(numero_dos, int)):
      return f"el resultado de la resta es: {resultado_resta}"
   return "Solo se permiten numeros enteros"
    
def multiplicar(numero_uno, numero_dos):
   resultado_multiplicar = numero_uno  * numero_dos
   if(isinstance(numero_uno, int) and isinstance(numero_dos, int)):
      return f"el resultado de la multiplicacion es: {resultado_multiplicar}"
   return "Solo se permiten numeros enteros"

def division(numero_uno, numero_dos):
   resultado_division = numero_uno / numero_dos
   if not (isinstance(numero_uno, int) and isinstance(numero_dos, int)):
      return "Solo se permiten numeros enteros"
   if(numero_dos == 0 ):
      return "no se puede devidir por 0."
   return f"la suma de los dos numeros es: {resultado_division}"

print("""Elige una operacion:
1. Sumar
2. Restar
3. Multiplicar
4. Division
""")
opcion = int(input("->"))
if(isinstance(opcion, int)): 
   if(opcion == 1):
      verdadero = False
      while verdadero:
         numero_uno = int(input("introduzca su primer numero:"))
         if not(isinstance(numero_uno, int)): 
          print("Solo se permite valores numericos")
         verdadero = True
   numero_dos = int(input("introduzca su segundo numero:"))
   sumar(numero_uno, numero_dos)