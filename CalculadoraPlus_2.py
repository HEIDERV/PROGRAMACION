import math

def menu():
    print("\nCALCULADORA CIENTIFICA")
    print("HEIDER VILLAMARIN\n")
    print("Seleccione una opción:")
    print("1 Sumar +")
    print("2 Restar -")
    print("3 Multiplicar *")
    print("4 Dividir /")
    print("5 Potencia **")
    print("6 Raíz cuadrada R")
    print("7 Factorial !")
    print("8 Salir X")

def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: No se puede dividir entre 0."

def potencia(x, y):
    return x ** y

def raiz_cuadrada(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo."
    
def factorial(num):
    if not isinstance(num, int) or num < 0:
        return "Error, el número debe ser un entero No Negativo"
    elif num == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, num + 1):
            resultado *= i
        return resultado

# Programa principal de las operaciones
while True:
    menu()
    opcion = input("Ingrese el número, la palabra o el símbolo de la operación deseada: ").upper() # upper permite convertir a MAYUSCULAS

    if opcion in ['1', 'SUMAR', '+']:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print(f"{num1} + {num2} = {sumar(num1, num2)}")
    elif opcion in ['2', 'RESTAR', '-']:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print(f"{num1} - {num2} = {restar(num1, num2)}")
    elif opcion in ['3', 'MULTIPLICAR', '*']:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
    elif opcion in ['4', 'DIVIDIR', '/']:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print(f"{num1} / {num2} = {dividir(num1, num2)}")
    elif opcion in ['5', 'POTENCIA', '**']:
        base = float(input("Ingrese la base: "))
        exponente = float(input("Ingrese el exponente: "))
        print(f"{base} ^ {exponente} = {potencia(base, exponente)}")
    elif opcion in ['6', 'RAIZ CUADRADA', 'R']:
        num = float(input("Ingrese el número para calcular su raíz cuadrada: "))
        print(f"La raíz cuadrada de {num} es: {raiz_cuadrada(num)}")
    elif opcion in ['7', 'FACTORIAL', '!']:
        num = int(input("Ingrese un numero para obtener su factorial: "))
        print(f"{factorial(num)}")
    elif opcion in ['8', 'SALIR', 'X']:
        print("TERMINADO")
        break
    else:
        print("Por favor, ingrese una opción válida.")