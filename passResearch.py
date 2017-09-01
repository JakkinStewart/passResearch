#! /usr/bin/env python
# Written by Joshua Jordi

import codecs
from sys import argv
import csv

avg = 0
count = 0
passList = []
password_dict = {}
# Reads everything in as UTF-8 (makes other languages easier to work with)
for password in codecs.open(argv[1], encoding='utf-8'):

    # Strips away newline characters since they are unnecessary and changes the string to a list of characters
    password = list(password.strip('\n'))

    # Helps calculate average length of password
    if len(password) > 0:

        length = len(password)
        avg += length
        count += 1
        characterNumber = 0

    # Creates a temporary list out of the password
    #templist = list(password)

    # Count the number of times a character shows up in a specific position
    password_list = list(password)
    for character in password:
        if character in password_dict:
            password_dict[character] += 1
        else:
            password_dict[character] = 1

print("Average length of password: %d\n" % (avg/count))
print("Password char dictionary")
#myprint(passtionary)

print(password_dict)

with open('password.csv', 'w') as f:
    [f.write('{0},{1}\n'.format(key, value)) for key, value in password_dict.items()]

#with open('password.csv', 'wb') as csv_file:
#    writer = csv.writer(csv_file)
#    for key, value in password_dict.items():
#        writer.writerow([key, value])

#with open('password.csv','wb') as f:
#    w = csv.writer(f)
#    w.writerow(password_dict.keys())
#    w.writerow(password_dict.values())

#for i in range(len(passtionary)):
#    print("Character: %d" % i)
#    print(passtionary[i])

#print(len(passtionary))

##print("upper %d" % UPPER)
##print("lower %d" % lower)
##print("Digit %d" % digit)
##print("Symbol %d" % symbol)
