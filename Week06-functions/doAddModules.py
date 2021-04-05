#this program will add students modules and grades
#it will keep reading until the user enters the name blank
#Author: Carolyn Moorhouse

def readModules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit):").strip()

    while moduleName != "":
        module = {}
        module ["name"] = moduleName
        module["grade"] = int(input("\t\tEnter grade:"))
        modules.append(module)
        moduleName = input("\tEnter next module name (blank to quit):").strip()

    return modules
    