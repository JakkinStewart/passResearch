#! /usr/bin/env python
# Written by Joshua Jordi

import codecs

avg = 0
count = 0
passtionary = {}
#UPPER = 0
#lower = 0
#digit = 0
#symbol = 0

# Reads everything in as UTF-8 (makes other languages easier to work with)
for password in codecs.open(input('Enter filename: '), encoding='utf-8'):

    # Strips away newline characters since they are unnecessary
    password = password.strip('\n')

    # If a password is longer than the length of the dictionary, extend the dictionary
    if len(passtionary) < len(password):
        difference = len(password) - len(passtionary)
        for i in range(difference):
            passtionary[i] = {}

    # Helps calculate average length of password
    if len(password) > 0:
        length = len(password)
        avg += length
        count += 1
        characterNumber = 0

    # Creates a temporary list out of the password
    templist = list(password)

    for i in range(len(password)):
        print(passtionary)
        if password[i] in passtionary[i]:
            passtionary[i][password[i]] += 1

        else:
            tempdict = {password[i]: 1}
            #passtionary[i].update(tempdict)
            passtionary[i].update(tempdict)


#    #for i in range(len(password)):
#    #    passtionary[i] = {}


#
#passwordCharacters = []
#passwordCharCount = []
#position = []
#
#
##print(passwordCharacters)
#passwordNum = 0

#    tempPassList = list(password.strip('\n'))
#    passwordCharacters.append([0] * len(password.strip('\n')))
#    passwordCharCount.append([0] * len(password.strip('\n')))
#
#    #charCount = 0
#    for i in range(len(tempPassList)):
#        #if tempPassList[i] in passwordCharacters:
#        #print(list(password.strip('\n')))
#        print(len(tempPassList))
#        print(i)
#
#        if tempPassList[i] in passwordCharacters[passwordNum]:
#            passwordCharCount[passwordNum][passwordCharacters[i].index(tempPassList[i])] += 1
#            #passwordCharCount[i]
#
#        else:
#            passwordCharacters[passwordNum][i] = tempPassList[i]
#            passwordCharCount[passwordNum][i] = 1
#
#        print(passwordCharacters)
#        #charCount += 1
#
##    charCount = 0
##    for character in password:
##        character = character.strip()
##        if character in passwordCharacters:
##            tempList = list(passwordCharacters[character])
##            print("THIS IS A LIST!!!" + tempList)
##            passwordCharacters[charCount].append(passwordCharacters[(character, tempList[1] + 1)])
##        else:
##            passwordCharacters.append((character, 1))
##
##    for character in password:
##        if character not in passwordCharacters:
##            passwordCharacters.append([character])
##        if character.isupper():
##            UPPER += 1
##        elif character.islower():
##            lower += 1
##            #if character is 'a':
##            #    passwordCharacters[characterNumber].append(character)
##        elif character.isdigit():
##            digit += 1
##        else:
##            symbol += 1
##        characterNumber += 1
#
########### Need to find a way to keep passwords in a list as I for loop them
########### Still need to find a way to check for symbols and find a way to enumerate them based on location in password (ie password[0], password[1], etc.
#
##print(passwordCharacters[0])
##print(passwordCharCount[0])
#
##for i in range(len(passwordCharacters)):
##    print("%s: %d" % (passwordCharacters[i], passwordCharCount[i]))
#
#
#print(passwordCharacters)


print("Average length of password: %d" % (avg/count))

for i in range(len(passtionary)):
    print(passtionary[i])
#print(len(passtionary))

##print("upper %d" % UPPER)
##print("lower %d" % lower)
##print("Digit %d" % digit)
##print("Symbol %d" % symbol)
