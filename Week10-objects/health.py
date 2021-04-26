#Use person module-following along with lecture 10
#Author: Carolyn Moorhouse

from personmodule import *

person1 = {
        'firstname' : 'Carolyn',
        'lastname' : 'Moorhouse',
        'dob' : dt.date(1990,7,6 ),
        'height': 180,
        'width': 100
    }
displayperson(person1)
gethealthdata(person1)