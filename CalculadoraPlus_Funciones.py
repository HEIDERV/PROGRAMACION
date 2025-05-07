# calculadora cientifica con funciones
print()
print ("MI CALCULADORA CIENTIFICA CON FUNCIONES") 
print ("HEIDER VILLAMARIN")

import math
def menu():
    print()
    print("Seleccione una opción:")
    print("1 Sumar +")
    print("2 Restar -")
    print("3 Multiplicar *")
    print("4 Dividir /")
    print("5 Potencia **")
    print("6 Raíz cuadrada R")
    print("7 Salir X")

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


# Programa principal de las operaciones
while True:

    menu()
    opcion = input("Ingrese el numero, la palabra o el simbolo de la operacion deseada: ")


    if opcion == '1' or opcion == 'SUMAR' or opcion == '+':
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print(f"{num1} + {num2} = {sumar(num1, num2)}")

    elif opcion == '2' or opcion == 'RESTAR' or opcion == '-':
       num1 = float(input("Ingrese el primer número: "))
       num2 = float(input("Ingrese el segundo número: "))
       print(f"{num1} - {num2} = {restar(num1, num2)}")

    elif opcion == '3' or opcion == 'MULTIPLICAR' or opcion == '*':
       num1 = float(input("Ingrese el primer número: "))
       num2 = float(input("Ingrese el segundo número: "))
       print(f"{num1} * {num2} = {multiplicar(num1, num2)}")

    elif opcion == '4'or opcion == 'DIVIDIR' or opcion == '/':
       num1 = float(input("Ingrese el primer número: "))
       num2 = float(input("Ingrese el segundo número: "))
       print(f"{num1} / {num2} = {dividir(num1, num2)}")

    if  opcion == '5' or opcion == 'POTENCIA' or opcion == '**':
          base = float(input("Ingrese la base: "))
          exponente = float(input("Ingrese el exponente: "))
          print(f"{base} ^ {exponente} = {potencia(base, exponente)}")

    elif opcion == '6'or opcion == 'RAIZ CUADRADA' or opcion == 'R':
          num = float(input("Ingrese el número para calcular su raíz cuadrada: "))
          print(f"La raíz cuadrada de {num} es: {raiz_cuadrada(num)}")

    elif opcion == '7'or opcion == 'SALIR' or opcion == 'X':
          print("TERMINADO")
    break
