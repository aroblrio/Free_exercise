#Voy a incluir la biblioteca math para hacer operaciones matematicas más complejas de lo habitual
import math

def cont_menu(i):
    if i != 1:
        print("Muchas gracias por usar el programa") 
i = 1
#He utilizado un bucle while para que el menu aparezca todas las veces que el usuario quiera sin tener que cargar el programa tantas veces
while i == 1:
#Aquí muestro el menú de la calculadora por pantalla
    print("Seleccione una opción: ")
    print("1: Sumar: ")
    print("2: Restar: ")
    print("3: Multiplicar: ")
    print("4: Dividir: ")
    print("5: Exponencial: ")
    print("6: Raices: ")
    print("7: Logaritmos: ")
    print("8: Seno: ")
    print("9: Coseno: ")
    print("10: Tangente: ")
#Le digo al usuario que me introduzca la opcion que él quiere
    n = int(input())
#En base a la opcion que elija el usuario, saldrá una opcion u otra        
    if n == 1:
        print("Introduce los números que quieres sumar: ")
        a = float(input())
        b = float(input())
        print(a+b)
    if n == 2:
        print("Introduce los números que quieres restar: ")
        a = float(input())
        b = float(input())
        print(a-b)
    if n == 3:
        print("Introduce los números que quieres multiplicar: ")
        a = float(input())
        b = float(input())
        print(a*b)
    if n == 4:
        print("Introduce los números que quieres dividir: ")
        a = float(input())
        b = float(input())
        print(a/b)
    if n == 5:
        print("Introduce la base de la potencia: ")
        a = float(input())
        print("Introduce el exponente: ")
        b = float(input())
        print(a**b)
    if n == 6:
        print("Introduce el radical: ")
        a = float(input())
        print("Introduce el radicando: ")
        b = float(input())
        print(b**(1/a))   
    if n == 7:
        print("Introduce la base del logaritmo: ")
        a = float(input())
        print("Introduce el argumento: ")
        b = float(input())
        print(math.log(b)/(math.log(a)))
    if n == 8:
        print("Introduce el ángulo en grados: ")
        a = float(input())
        a = math.radians(a)
        print(math.sin(a))
    if n == 9:
        print("Introduce el ángulo en grados: ")
        a = float(input())
        a = math.radians(a)
        print(math.cos(a))
    if n == 10:
        print("Introduce el ángulo en grados: ")
        a = float(input())
        a = math.radians(a)
        print(math.tan(a))
    print("¿Deseas continuar? ")
    print("1: Si ")
    print("2: No ")
    i = int(input())
    cont_menu(i)
    
    




   














