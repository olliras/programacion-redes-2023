'''
Descripcion: Consumiendo API con Python
Autor: samuel reynaldo olvera lira
Fecha: 20 de octubre del 2023

'''

import urllib.parse
import requests

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        #Mensaje de despedida
        print("Mensaje de despedida")
        break
    
    dest = input("Destination: ")
        #Mensaje de despedida
    if dest == "quit" or dest == "q":
        print("Mensaje de despedida")
    break
    
    
    
    

    main_api = "https://www.mapquestapi.com/directions/v2/route?"

    key = "1ejRd0KasJblqLfvQZCk8ZJhgwsLPrHx"

    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    json_data = requests.get(url).json()

    print("URL: " + (url))  

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

  