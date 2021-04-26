#demonstration of a module following along with lecture 10
#Author: Carolyn Moorhouse
import datetime as dt
def gethealthdata(person):
    print("get health data: ", person['firstname'])

def displayperson(person):
    print(person)

if __name__ == '__main__':
    person1 = {
        'firstname' : 'Carolyn',
        'lastname' : 'Moorhouse',
        'dob' : dt.date(1990,7,6 ),
        'height': 180,
        'width': 100
      }
    displayperson(person1)
    gethealthdata(person1)