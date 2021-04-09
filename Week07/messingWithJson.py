#messing with json along to lecture 7
#Author: Carolyn Moorhouse
import json


electricBill = {
    'name' : 'Carolyn',
    'Amount' : '999'
}

with open("storeData.json", "w") as f:
 #   json.dump(electricBill, f)

with open("storeData.json", "rt") as f:
    readDict = json.load(f)
    print (readDict["name"])

     