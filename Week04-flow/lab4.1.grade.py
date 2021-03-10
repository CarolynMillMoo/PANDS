#This program reads in a students percentage
#and prints out the corresponding grade

#Author: Carolyn Moorhouse

percentage = float(input("Enter the percentage: "))
round(percentage)

if percentage < 0 or percentage > 100:
    print("Please enter a number between 0 and 100")

elif percentage < 40:
    print ("Fail")
elif percentage < 50:
    print ("Pass")
elif percentage < 60:
    print ("Merit1")
elif percentage < 70:
    print ("Merit2")
else: #the only valid percentage remaining is between 70 and 100
    print ("Distinction")
