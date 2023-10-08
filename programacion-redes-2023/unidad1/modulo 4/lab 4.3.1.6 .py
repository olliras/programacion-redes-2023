'''
nombre: Samuel reynaldo olvera lira
fecha: 6 de octubre 2023
descripcion: laborartorios modulo 4
'''
def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

