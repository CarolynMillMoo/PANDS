#this program reads in a string and strips any leading
#or trailing spaces. it also converts all the letters
#to lower case. this program als outputs the length of the 
#the orginal string and the normalised one.
#author@ Carolyn Moorhouse

rawString = input("Please enter a string:")
normalisedString = rawString.strip().lower()

lengthOfRawString = len(rawString)
lengthOfNormalised = len(normalisedString)

print("That String normalised is: {}".format(normalisedString))
print("We reduced the input string from {} to {} characters".format(lengthOfRawString, lengthOfNormalised))
