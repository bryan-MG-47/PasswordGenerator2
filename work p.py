import json

fdata='efegrgrgrhttgrgrdgbd'
nameD='facebook'

def WriteInJsonFile(fdata,nameD):

    with open('savePass.json', 'w') as outfile:
        json.dump({nameD:fdata}, outfile)

WriteInJsonFile(fdata,nameD)
