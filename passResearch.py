#! /usr/bin/env python
# Written by Joshua Jordi

import codecs
from sys import argv

avg = 0
count = 0
passList = []

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

    # If a password is longer than the length of the dictionary, extend the dictionary

    for i in range(len(password)):
        #print(passtionary)

        if len(passList) < len(password):
            difference = len(password) - len(passList)
            for i in range(difference):
                passList.append({})

        if password[i] in passList[i]:
            passList[i][password[i]] += 1

        else:
            tempdict = {password[i]: 1}
            #passtionary[i].update(tempdict)
            passList[i] = tempdict


print("Average length of password: %d" % (avg/count))

print(passList)
#myprint(passtionary)

#for i in range(len(passtionary)):
#    print("Character: %d" % i)
#    print(passtionary[i])

#print(len(passtionary))

##print("upper %d" % UPPER)
##print("lower %d" % lower)
##print("Digit %d" % digit)
##print("Symbol %d" % symbol)
