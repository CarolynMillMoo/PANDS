#This program generates a random number between 1 and 100
#for the user to guess
#the program will prompt the user when the guess is too low or too high
#Author: Carolyn Moorhouse

import random
#used the random integer module from lab 2.3 and modified to suit this program
number = random.randint(1,100)

guess = int(input("Please guess the number:"))
while guess != number:
   if guess < number:
      print("Too Low!")
   else:
      print("Too High!")
   guess = int(input("Please guess again:"))

print("Well done! Yes the number was ", format(number))