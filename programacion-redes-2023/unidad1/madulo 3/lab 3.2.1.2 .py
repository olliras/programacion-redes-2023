'''
nombre: Samuel reynaldo olvera lira
fecha: 26 de septiembre 2023
descripcion: laborartorios modulo 2
'''
odd_numbers = 0
even_numbers = 0

while True:
    number = int(input("Introduce un número o escribe 0 para detener: "))
    
    if number == 0:
        break  # Salir del bucle si se ingresa 0
    
    if number % 2 == 1:
        odd_numbers += 1
    else:
        even_numbers += 1

print("Cuenta de números impares:", odd_numbers)
print("Cuenta de números pares:", even_numbers)
