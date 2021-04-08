#A different method of dealing with the users choice
#this program stores/displays students names, modules and grades.
#Author: Carolyn Moorhouse

def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()
    return choice

def doAdd(students):
    print("do add")
def doView(students):
    print("do view")
def doNothing(dumby):
    pass

#the dict that maps a letter to function
choiceMap = {
    'a': doAdd(students),
    'v': doView(students),
    'q': doNothing(dumby)
}

#main program
students = []
choice = displayMenu()
while(choice != 'q'):
    if choice in choiceMap:
        #run the function
        choiceMap[choice] (students)
    else: #if the user enters something which is not valid
        print("\n\nplease select either a, v, or q")

    choice=displayMenu()


