

import json



#Create an empty list
jsonlist = []

def MyFunctionToRecover(Nom):
    with open("savedPass.json", "r") as infile:
        jsonData = json.load(infile)
        jsonlist = jsonData[Nom]
    print(jsonlist)

MyFunctionToRecover("nom1")    

