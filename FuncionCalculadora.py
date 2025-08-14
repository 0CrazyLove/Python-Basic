def sumar(numero_uno, numero_dos):
    resultado = numero_uno + numero_dos
    if(isinstance(numero_uno, int) and isinstance(numero_dos, int)):
     return f"la suma de los dos numeros es: {resultado}"
    return "Solo se permiten numeros enteros"
print(sumar("hl","lol"))