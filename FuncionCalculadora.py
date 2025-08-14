# funciones
def sumar(numero_uno, numero_dos):
    resultado_suma = numero_uno + numero_dos
    if isinstance(numero_uno, int) and isinstance(numero_dos, int):
        return f"la suma de los dos numeros es: {resultado_suma}"
    return "Solo se permiten numeros enteros"


print(sumar("hl", "lol"))


def restar(numero_uno, numero_dos):
    resultado_resta = numero_uno - numero_dos
    if isinstance(numero_uno, int) and isinstance(numero_dos, int):
        return f"el resultado de la resta es: {resultado_resta}"
    return "Solo se permiten numeros enteros"


def multiplicar(numero_uno, numero_dos):
    resultado_multiplicar = numero_uno * numero_dos
    if isinstance(numero_uno, int) and isinstance(numero_dos, int):
        return f"el resultado de la multiplicacion es: {resultado_multiplicar}"
    return "Solo se permiten numeros enteros"


def division(numero_uno, numero_dos):
    resultado_division = numero_uno / numero_dos
    return f"la division de los dos numeros es: {resultado_division}"


# menu
while True:
    opcion = None
    print(
        """Elige una operacion:
    1. Sumar
    2. Restar
    3. Multiplicar
    4. Division
    """
    )
    try:
        opcion = int(input("->"))
        break
    except ValueError:
        print("solo se permite valores numericos.")
# funcion sumar
if opcion == 1:
    while True:
        try:
            numero_uno = int(input("introduzca su primer numero:"))
            break
        except ValueError:
            print("Solo se permite valores numericos")

    while True:
        try:
            numero_dos = int(input("introduzca su segundo numero:"))
            break
        except ValueError:
            print("Solo se permite valores numericos.")

    print(sumar(numero_uno, numero_dos))

# funcion restar
if opcion == 2:
    while True:
        try:
            numero_uno = int(input("introduzca su primer numero:"))
            break
        except ValueError:
            print("Solo se permite valores numericos")

    while True:
        try:
            numero_dos = int(input("introduzca su segundo numero:"))
            break
        except ValueError:
            print("Solo se permite valores numericos.")

    print(restar(numero_uno, numero_dos))
# funcion multiplicar
if opcion == 3:
    while True:
        try:
            numero_uno = int(input("introduzca su primer numero:"))
            break
        except ValueError:
            print("Solo se permite valores numericos")

    while True:
        try:
            numero_dos = int(input("introduzca su segundo numero:"))
            break
        except ValueError:
            print("Solo se permite valores numericos.")

    print(multiplicar(numero_uno, numero_dos))
# funcion dividir
if opcion == 4:
    while True:
        try:
            numero_uno = int(input("introduzca su primer numero:"))
            break
        except ValueError:
            print("Solo se permite valores numericos")

    while True:
        try:
            numero_dos = int(input("introduzca su segundo numero:"))
            if(numero_dos == 0): 
             print("no se puede dividir por 0")
             continue #estudiar esto y lo de break de abajo
            break
         
        except ValueError:
            print("SoLo se permite valores numericos.")
            
    print(division(numero_uno, numero_dos))
