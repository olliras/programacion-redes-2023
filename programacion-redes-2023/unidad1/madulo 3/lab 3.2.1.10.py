'''
nombre: Samuel reynaldo olvera lira
fecha: 2 de octubre 2023
descripcion: laborartorios modulo 3
'''

# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable user_word.
user_word = input("Ingresa una palabra: ")

# Convertir la palabra ingresada a mayúsculas
user_word = user_word.upper()

# Iterar a través de cada letra en la palabra
for letter in user_word:
    # Verificar si la letra es una vocal
    if letter in "AEIOU":
        # Si es una vocal, omitir esta iteración y continuar con la siguiente letra
        continue
    # Si no es una vocal, imprimir la letra
    print(letter)
