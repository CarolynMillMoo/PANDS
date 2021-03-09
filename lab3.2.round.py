#Rounds a number to the nearest even number
#e.g. 4.5 rounds to 4
#but 5.5 rounds to 6
#not to be used if accuracy is essential
#Author: Carolyn Moorhouse

numberToRound = float (input("Enter a float number:"))
roundedNumber = round(numberToRound)
print ('{} rounded is {}'.format(numberToRound, roundedNumber))

