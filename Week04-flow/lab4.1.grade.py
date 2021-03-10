#This program reads in a students percentage
#and prints out the corresponding grade

#Author: Carolyn Moorhouse

percentage = float(input("Enter the percentage: "))

if percentage < 0 or percentage > 100:
    print("Please enter a number between 0 and 100")

elif percentage < 39.5:
    print ("Fail")
elif percentage < 49.5:
    print ("Pass")
elif percentage < 59.5:
    print ("Merit1")
elif percentage < 69.5:
    print ("Merit2")
else: #the only valid percentage remaining is between 70 and 100
    print ("Distinction")
