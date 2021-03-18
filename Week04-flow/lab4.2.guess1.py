#program that prompts the user to guess a number
#the program should keep prompting the user to guess until the user gets the right one
#Author: Carolyn Moorhouse

numberToGuess = 28

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    print ("Wrong!!")
    guess = int(input("Please guess again:"))

print("Well done! Yes the number was ", numberToGuess)

