import csv 
import os
import json
#print(os.getcwd())

def FiltrarCasosConfirmados():
    file =  open("casos.csv",encoding="utf16")
    data = csv.reader(file)
    filtrados = []
    claves = next(data)
    # print(claves)
    count=0
    d={}
    for i in data:
        # separamos primero por las provincias
        if i[20]=="Confirmado":
            provincia = i[5]
            fecha = i[9]
            if provincia in d.keys():
                if fecha in d[provincia].keys():
                    d[provincia][fecha]+=1
                else:
                    d[provincia][fecha]=1
            else:    
                d[provincia]={fecha:1}
    total_general=0
    for provincia,casos in d.items():
        total=sum(casos.values())
        total_general+=total
        d[provincia]["total"]=total
    d["total_general"]=total_general
    with open("yessi.json","w",encoding="utf8") as file:
        json.dump(d,file,indent=4,ensure_ascii=False)

#FiltrarCasosConfirmados()

def obtenerConfirmadosPorProvincia(provincia):
    with open("yessi.json",encoding="utf8") as file:
        data=json.load(file)

    with open(provincia+"-Confirmados.json","w",encoding="utf8") as file:
        json.dump(data[provincia],file,indent=4)

obtenerConfirmadosPorProvincia("Buenos Aires")    
obtenerConfirmadosPorProvincia("Córdoba")    
obtenerConfirmadosPorProvincia("CABA")    

def FiltrarDatosPorProvincia():
    file =  open("data.csv",encoding="utf16")
    data = csv.reader(file)
    filtrados = []
    claves = next(data)
    #print(claves)

    for i in data:
        #separamos primero por las provincias
        d={}
        if i[1]=="Buenos Aires" or i[1]=="CABA" or i[1]=="Córdoba":
            for k in range(len(i)):
                d.setdefault(claves[k],i[k])
            filtrados.append(d.copy())

    #print(filtrados)

    with open("filtrados.json","w",encoding="utf8") as file:
        json.dump(filtrados,file,indent=4,ensure_ascii=False)



def FiltrarDatosParticularesProvincia(provincia=""):
    if provincia == "":
        print("Tenes que ingresar un parametro de la provincia")
        exit(1)

    with open("filtrados.json",encoding="utf8") as file:
        data=json.load(file)
    filtrado = []
    for i in data:
        if i["provincia"] == provincia:
            filtrado.append({"fecha":i["fecha"],"positivos":int(i["positivos"] if i["positivos"]!="" else 0 ),"total":int(i["total"] if i["total"]!="" else 0 )})


    with open(provincia+".json","w") as file:
        json.dump(filtrado,file,indent=4)

# FiltrarDatosParticularesProvincia("Buenos Aires")        
# FiltrarDatosParticularesProvincia("CABA")        
# FiltrarDatosParticularesProvincia("Córdoba")

def ObtenerDatosDiaADiaPorProvincia(provincia=""):
    if provincia == "":
        print("debe ingresar el nombre de una provincia para obtener los datos")
        exit(1)
    # provincia="Buenos Aires"

    with open(provincia+".json",) as file:
        data = json.load(file)
        # json.dump(filtrado,file,indent=4)\
    datos = {}
    for i in data:
        if i["fecha"] in datos.keys():
            datos[i["fecha"]]["positivos"] = sum([datos[i["fecha"]]["positivos"],i["positivos"]])
            datos[i["fecha"]]["total"] = sum([datos[i["fecha"]]["total"],i["total"]])
        else:
            datos[i["fecha"]] = {"positivos":i["positivos"],"total":i["total"]}

    with open(provincia+"-Dia_a_Dia.json","w") as file:
        json.dump(datos,file,indent=4)

# ObtenerDatosDiaADiaPorProvincia("Buenos Aires")        
# ObtenerDatosDiaADiaPorProvincia("CABA")        
# ObtenerDatosDiaADiaPorProvincia("Córdoba")


