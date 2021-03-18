#this program keeps reading inputted numbers 
#until 0 is inputted.
#once 0 is inputted a print out of the numbers entered
#and the average of the them.
#Author: Carolyn Moorhouse

numbers = []

#first number then we check if it is 0 in the while loop
number = int(input("Enter number (0 to quit): "))

while number != 0:
    numbers.append(number)

    #read the next number and check if 0
    number = int(input("Enter another (0 to quit): "))

for value in numbers:
    print (value)

#I want the average to be a float
average = float(sum(numbers)) / len(numbers)
print ("The average is {}".format(average))

