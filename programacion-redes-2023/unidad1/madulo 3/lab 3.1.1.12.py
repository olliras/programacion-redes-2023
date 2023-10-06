'''
nombre: Samuel reynaldo olvera lira
fecha: 2 de octubre 2023
descripcion: laborartorios modulo 3
'''
year = int(input("Introduce un año:"))
if year < 1582:
    print("No está dentro del período del calendario Gregoriano")
else:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Año Bisiesto")
    else:
        print("Año Común")
