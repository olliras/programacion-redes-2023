'''
nombre: Samuel reynaldo olvera lira
fecha: 2 de octubre 2023
descripcion: laborartorios modulo 3
'''

number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))

largest_number = number1

if number2 > largest_number:
    largest_number = number2

if number3 > largest_number:
    largest_number = number3

# Imprime el resultado
print("El número más grande es:", largest_number)
