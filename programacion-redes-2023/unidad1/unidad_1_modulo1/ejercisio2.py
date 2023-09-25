'''
nombre: samuel reynaldo olvera lira
descripcion: ejercisios modulo 1
fecha: 22 de septiembre
'''
n = int(input("Ingrese un entero positivo: "))


if n <= 0:
    print("Por favor, ingrese un entero positivo.")
else:
    

 
    for i in range(1, n + 1):
        suma += i
    print(f"La suma de los enteros desde 1 hasta {n} es: {suma}")
