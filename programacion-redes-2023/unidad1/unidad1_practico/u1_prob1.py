'''
nombre: Samuel reynaldo olvera lira
fecha: 2 de octubre 2023
descripcion: problema 1 
'''
#soy par 
monto_inicial = float(input("Ingrese la cantidad de dinero depositada: "))

interes_anual = 0.04
saldo_1_anos = monto_inicial * (1 + interes_anual)
saldo_2_anos = saldo_1_anos * (1 + interes_anual)
saldo_3_anos = saldo_2_anos * (1 + interes_anual)

print(f"Saldo después de 1 año: {round(saldo_1_anos, 2)}")
print(f"Saldo después de 2 años: {round(saldo_2_anos, 2)}")
print(f"Saldo después de 3 años: {round(saldo_3_anos, 2)}")

 
