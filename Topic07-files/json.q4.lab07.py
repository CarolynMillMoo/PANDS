#a function that will read in a dict object from file
#Author: Carolyn Moorhouse

import json
filename = "testdict.json"

def readDict():
    with open(filename) as f:
        return json.load(f)

somedict = readDict()
print(somedict)

#Tested and worked