'''
nombre: Samuel reynaldo olvera lira
fecha: 9 de octubre 2023
descripcion: ejercsio practico
'''

lstnombres = []
for i in range(5):
    nombre = input(f"Ingresa el nombre del amigo {i+1}:  ")
    lstnombres.append(nombre)

lstedades = []
for i in range(5):
    edad = int(input(f"Ingresa la edad de {lstnombres[i]}:  "))
    lstedades.append(edad)

dicDatos = {}
for i in range(5):
    dicDatos[lstnombres[i]] = lstedades[i]

def mostrar_datos(diccionario):
    for nombre, edad in diccionario.items():
        print(f"{nombre} -> {edad}")

print("Contenido del diccionario:")
mostrar_datos(dicDatos)

print(f"Longitud de lstnombres: {len(lstnombres)}")
print(f"Longitud de lstedades: {len(lstedades)}")
print(f"Longitud de dicDatos: {len(dicDatos)}")

print("Claves del diccionario ordenadas:")
claves_ordenadas = sorted(dicDatos.keys())
for clave in claves_ordenadas:
    print(clave)

def buscar_nombre(diccionario, clave):
    if clave in diccionario:
        return diccionario[clave]
    else:
        return None
nombre_buscar = input("pon tu  nombre para buscar en el diccionario: ")
resultado = buscar_nombre(dicDatos, nombre_buscar)
if resultado is not None:
    print(f"{nombre_buscar} tienes {resultado} años ")  
else:
    print(f"{nombre_buscar} no se encuentra en el diccionario ")
