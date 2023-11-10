'''
Descripcion: Consumiendo API con Python
Autor: samuel reynaldo olvera lira
Fecha: 20 de octubre del 2023

'''
import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Dolores Hidalgo"
dest = "San Miguel de Allende"
key = "1ejRd0KasJblqLfvQZCk8ZJhgwsLPrHx"  

url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
print(url)

json_data = requests.get(url).json()

# Comprueba si la solicitud fue exitosa
if json_data['info']['statuscode'] == 0:
    # Extrae la distancia y el tiempo
    print("Tiempo:", json_data['route']['formattedTime'])
    print("Distancia:", json_data['route']['distance'])
    # Extrae el campo formattedTime del primer elemento de legs
    print("Tiempo formateado:", json_data['route']['legs'][0]['formattedTime'])
else:
    print("Error en la solicitud:", json_data['info']['messages'][0])




