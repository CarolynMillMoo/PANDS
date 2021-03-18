#Program which prompts the user to guess a number
#The program will keep prompting the user until they guess correctly
#this program will also give hints to the user, i.e if their guess is too high or too low
#Author: Carolyn Moorhouse

numberToGuess = 28

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
   if guess < numberToGuess:
      print("Too Low!")
   else:
      print("Too High!")
   guess = int(input("Please guess again:"))

print("Well done! Yes the number was ", numberToGuess)
