# La key es 6be8ade3d39242a818296daa9bf6ee22
import requests
import os
headers={"Accept":"application/json","user-key":os.environ["key"]}
URL_BASE="https://developers.zomato.com/api/v2.1/"

payload={"q":"New York"}
r=requests.get(URL_BASE+"cities",headers=headers,params=payload)
if r.status_code==200:
	datos=r.json()
	id=datos["location_suggestions"][0]["id"]

print("Colecciones\n")
payload={"city_id":id}
r=requests.get(URL_BASE+"collections",headers=headers,params=payload)
if r.status_code==200:
	datos=r.json()
	for coleccion in datos["collections"]:
		print(coleccion["collection"]["title"])

print("Tipos de cocina\n")
r=requests.get(URL_BASE+"cuisines",headers=headers,params=payload)
if r.status_code==200:
	datos=r.json()
	for coleccion in datos["cuisines"]:
		print(coleccion["cuisine"]["cuisine_name"])

print("Tipos de establecimentos\n")
r=requests.get(URL_BASE+"establishments",headers=headers,params=payload)
if r.status_code==200:
	datos=r.json()
	for establecimiento in datos["establishments"]:
		print(establecimiento["establishment"]["name"])
