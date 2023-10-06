'''
nombre: Samuel reynaldo olvera lira
fecha: 2 de octubre 2023
descripcion: laborartorios modulo 3
'''
income = float(input("Introduce el ingreso anual:"))

if income <= 85528:
    tax = 0.18 * income - 556.02
else:
    tax = 14839.02 + 0.32 * (income - 85528)

# Redondear el impuesto a pesos enteros
tax = round(tax)

# Asegurarse de que el impuesto no sea negativo
if tax < 0:
    tax = 0

print("El impuesto es:", tax, "pesos")
