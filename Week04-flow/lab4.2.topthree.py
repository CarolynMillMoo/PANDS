#This program generates 10 random numbers.
#prints them our, then
#prints out the top 3

#A list will be used to store and 
#manipulate the numbers

import random
#programming the general case
howMany = 10
topHowMany = 3
rangeFrom = 0
rangeTo = 100

numbers = []

for i in range(0,10):
    numbers.append(random.randint(rangeFrom, rangeTo))
print("{} random numbers\t {}".format(howMany,numbers))

topOnes = numbers.copy()
topOnes.sort(reverse = True)
print ("The top {} are \t\t {}".format(topHowMany, topOnes[0:topHowMany]))
