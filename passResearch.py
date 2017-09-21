#! /usr/bin/env python
# Written by Joshua Jordi

import codecs
from sys import argv

avg = 0
count = 0
passList = [{}]

# Reads everything in as UTF-8 (makes other languages easier to work with)

# for password in codecs.open(argv[1], encoding='utf-8'):
with codecs.open(argv[1], encoding='utf-8') as f:
    while True:

        content = f.readlines(1000)
        if not content:
            break
        content = [password.strip('\n') for password in content]
        # Strips away newline characters since they are unnecessary and changes
        # the string to a list of characters
        # password = list(password.strip('\n'))
        # password = password.strip('\n')

        for password in content:
            if len(password) > 0:
                length = len(password)
                avg += length
                count += 1

            for index in range(0, len(password)):
                # if a dictionary doesn't exist for that character, make one
                if len(passList) <= index:
                    passList.append({})
                # if the character at that index doesn't exist, initialize it
                if password[index] not in passList[index].keys():
                    (passList[index])[password[index]] = 1
                # if it does exist, add to it
                else:
                    # (passList[index])[password[index]] = \
                    #    (passList[index])[password[index]] + 1
                    (passList[index])[password[index]] += 1


print(passList)
print("Average length of password: %d\n" % (avg/count))

for thing in passList:
    print(thing)

# with open('password.csv', 'w') as f:
#     [f.write('{0},{1}\n'.format(key, value)) for key, value in
#      passList.items()]
