#This program asks the user to enter a number
#the program will then tell the user if the number is even or odd

#Author: Carolyn Moorhouse

number = int(input("Enter an number:"))

if (number % 2) == 0 :
    print("{} is an even number".format(number))

else:
    print("{} is an odd number".format(number))
    