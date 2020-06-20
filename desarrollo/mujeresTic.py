import csv
import codecs
import json, os

def formatoLista():
	file =  open("dataMujeres.csv",encoding="utf8")
	data = csv.reader(file)
	with open("chicasEnTIC.json","w",encoding="utf8") as file:
		index = 0		
		for dato in data:	
			index += 1
			nombre = "dato" + str(index) + " = "
			json.dump(nombre, file,indent=4,ensure_ascii=False)
			json.dump(dato,file,indent=4,ensure_ascii=False)

formatoLista()

