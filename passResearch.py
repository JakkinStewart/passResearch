#! /usr/bin/env python
# Written by Joshua Jordi

import codecs
from sys import argv

avg = 0
count = 0
passList = []
password_dict = {}

# Reads everything in as UTF-8 (makes other languages easier to work with)
for password in codecs.open(argv[1], encoding='utf-8'):

    # Strips away newline characters since they are unnecessary and changes the
    # string to a list of characters
    # password = list(password.strip('\n'))
    password = password.strip('\n')

    # Helps calculate average length of password
    if len(password) > 0:
        length = len(password)
        avg += length
        count += 1

    if len(password) > len(passList):
        for i in range(len(password) - len(passList)):
            passList += []
            print(passList)

#         if not passList:
#             for i in range(len(password)):
#                 passList.append([])
#
#     print(passList)
#     print("Pass: " + password)
#     # Creates a temporary list out of the password
#     # templist = list(password)
#
#     # Count the number of times a character shows up in a specific position
#     try:
#         for i in range(len(password)):
#             if password[i] in passList[i]:
#                 print("password is in passList")
#                 # passList[i][password[i]] += 1
#             else:
#                 print('password is not in passList')
#                 passList.append({password[i]: 1})
#                 # passList[i][password[i]] = 1
#             # if character in password_dict:
#             #     password_dict[character] += 1
#             # else:
#             #     password_dict[character] = 1
#     except IndexError:
#         print("IndexError")
#         for i in range(len(password) - len(passList)):
#             passList.append([])
#         print(passList)


print(passList)
print("Average length of password: %d\n" % (avg/count))
print("Password char dictionary")
print(password_dict)

with open('password.csv', 'w') as f:
    [f.write('{0},{1}\n'.format(key, value)) for key, value in
     password_dict.items()]
