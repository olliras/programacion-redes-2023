'''
nombre: Samuel reynaldo olvera lira
fecha: 2 de octubre 2023
descripcion: laborartorios modulo 3
'''
secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle! |
| Introduce un número entero      |
| y adivina qué número he         |
| elegido para ti.                |
| Entonces,                       |
| ¿Cuál es el número secreto?     |
+==================================+
""")

while True:
    user_number = int(input("Ingresa un número: "))
    
    if user_number == secret_number:
        print("¡Bien hecho, muggle! Eres libre ahora")
        break
    else:
        print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
