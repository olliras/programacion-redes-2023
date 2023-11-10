'''
Descripcion: Consumiendo API con Python
Autor: samuel olvera lira
Fecha: 20 de octubre del 2023


'''
import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "San Ocote"
dest = "San Miguel de Allende"
key = "1ejRd0KasJblqLfvQZCk8ZJhgwsLPrHx"

url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
print("URL: " + url)

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.")
else:
    print("API Status: " + str(json_status) + " = A failed route call.")
