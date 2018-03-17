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

print("Restaurantes\n")

numero=0
resp=" "
while resp==" ":
	payload={"entity_id":id,"entity_type":"city","start":str(numero)}
	r=requests.get(URL_BASE+"search",headers=headers,params=payload)
	if r.status_code==200:
		datos=r.json()
		print("Encontrados: %d"%datos["results_found"])
		for restaurante in datos["restaurants"]:
			print(restaurante["restaurant"]["name"])
	numero=numero+20
	resp=input("Pulsa espacio para mostrar más restaurantes. Otra tecla para salir")


