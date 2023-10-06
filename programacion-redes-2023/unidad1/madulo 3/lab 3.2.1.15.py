'''
nombre: Samuel reynaldo olvera lira
fecha: 2 de octubre 2023
descripcion: laborartorios modulo 3
'''
# Pedir al usuario que ingrese un número natural
c0 = int(input("Ingresa un número natural: "))

# Inicializar la variable para contar los pasos
pasos = 0

# Iterar mientras c0 no sea igual a 1
while c0 != 1:
    # Imprimir el valor actual de c0
    print(c0)
    
    # Verificar si c0 es par o impar y actualizar su valor
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1
    
    # Incrementar el contador de pasos
    pasos += 1

# Imprimir el último valor (1) y el número total de pasos
print(1)
print("pasos =", pasos)
