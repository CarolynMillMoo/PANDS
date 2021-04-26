#Following along with lecture09. Demonstrate an exception
#this program prompts the user for a number and 
#returns that number multiplied by 2
#Author: Carolyn Moorhouse

try:
  inputVar = input('Enter a number:')
  number = int(inputVar)
  if (number <0):
      raise ValueError("Negative value entered")
  print('Number multiplied by 2 is:', number *2)
except ValueError as e:
    print("Please enter a  positive number")
    print (e)