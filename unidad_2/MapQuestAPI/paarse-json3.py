
'''
Descripcion: Consumiendo API con Python
Autor: samuel reynaldo olvera lira
Fecha: 20 de octubre del 2023

'''

import urllib.parse
import requests

while True:
    orig = input("Starting Location:  ")
    dest = input("Destination:  ")

    main_api = "https://www.mapquestapi.com/directions/v2/route?"
    key = "1ejRd0KasJblqLfvQZCk8ZJhgwsLPrHx"

    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    json_data = requests.get(url).json()

    print("URL: " + url)

    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successfull route call.\n")
    else:
        print("API Status: " + str(json_status) + " = A fallo route call.\n")
