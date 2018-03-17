# La key es 6be8ade3d39242a818296daa9bf6ee22
import requests
import os
headers={"Accept":"application/json","user-key":os.environ["key"]}
URL_BASE="https://developers.zomato.com/api/v2.1/"
r=requests.get(URL_BASE+"categories",headers=headers)
if r.status_code==200:
	datos=r.json()
	for categoria in datos["categories"]:
		print(categoria["categories"]["name"])