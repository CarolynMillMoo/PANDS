#Messing with functions along with lecture 6
#Anonymous functions
#Author: Carolyn Moorhouse

isMax = False
if isMax:
   fun = lambda num : num*2
else:
   fun = lambda num : num*3

var = fun(10)
print(var)

#sorted
list = [22, 33, 11, 1, 14]
print (list)
newList = sorted (list)
print(newList)

#sort dictionary
data = [{'first': 'Guido', 'last': 'Van Rossum', 'YOB': 1956},
        {'first': 'Grace', 'last': 'Hopper', 'YOB': 1906},
        {'first': 'Alan', 'last': 'Turing', 'YOB': 1912}]

def sortFun(item):
    print("in sortFun")
    return item['YOB']

#print(data)
newData = sorted(data, key = lambda item : item['last'])
for item in newData:
    print(item)