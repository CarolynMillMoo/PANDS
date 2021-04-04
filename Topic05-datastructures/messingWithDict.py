#Messing along with dictionaries lecture
#Author: Carolyn Moorhouse

car = {
    "make":"ford",
    "price": 123,
    "owner": {
        "firstName":"fred",
        "age": 12
    }
    }



print(type(car))
print (car)

car["model"]= "focus"
print(car)
#make = car["make"]
#notMake = car.get(ahfiusgriue)
#print (notMake)
#print (make)
print(car["owner"]["age"])