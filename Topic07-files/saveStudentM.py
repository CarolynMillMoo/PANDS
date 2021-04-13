#Using Student management program from week06
#create a new menu item called save
#Author: Carolyn Moorhouse
import json
students = []
filename="students.json"
def writeDict(obj):
    with open(filename, 'wt') as f:
        json.dump(obj,f)

def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(s) Save students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/s/q):").strip()
    return choice

def doAdd(students):
    currentStudent = {}
    currentStudent ["name"] = input("Enter name: ")
    currentStudent ["modules"] = readModules()
    students.append(currentStudent)
    print("in adding")

def readModules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit):").strip()

    while moduleName != "":
        module = {}
        module ["name "] = moduleName
        module ["grade"] = int(input("\t\tEnter grade:"))
        modules.append(module)
        moduleName = input("\tEnter next module name (blank to quit):").strip()
    return modules

def displayModules(modules):
    print("\tName       \tGrade")
    for module in modules:
       print("\t{}   \t{}".format(module["name "], module["grade"]))

def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"])
        print("in viewing")

def doSave(students):
    writeDict(students)
    print("students saved")

#main program
choice = displayMenu()
while(choice != 'q'):
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice == 's':
        doSave(students)
    elif choice !=  'q':
        print("\n\nplease select either a, v, s or q")
    choice=displayMenu()