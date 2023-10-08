'''
nombre: Samuel reynaldo olvera lira
fecha: 6 de octubre 2023
descripcion: laborartorios modulo 4
'''
def liters_100km_to_miles_gallon(liters):
    gallons = liters / 3.785411784
    miles = 100 / (gallons * 0.621371192)
    return miles

def miles_gallon_to_liters_100km(miles):
    kilometers = miles * 1.609344
    liters = 100 / (kilometers * 0.621371192)
    return liters

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.0))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
