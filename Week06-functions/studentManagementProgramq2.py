#this program allows a user to add new students 
#and view students, this information includes their modules and grades
#Author: Carolyn Moorhouse

def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()

    return choice
#Test the function
choice = displayMenu()
print("You chose {}".format(choice))