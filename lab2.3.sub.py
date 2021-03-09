#this code read two numbers and subtracts the first one from the second one
#author: Carolyn Moorhouse

#input reads in a string so this has to be converted to an int
#so mathematical operations can be performed

x = int(input("Enter first number: "))
y = int (input("Enter second number: "))
answer = x-y
print("{} minus {} is {}".format(x, y, answer))
