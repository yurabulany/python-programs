import random
import string

passwordLenght = 12  # can be any number

lowCaseLetters = list(string.ascii_lowercase)
upperCaseLetters = list(string.ascii_uppercase)
numbers = list(string.digits)
symbols = list(string.punctuation)

ifNumbers = True
ifSymbols = True

finalArray = []
finalPassword = []

if ifNumbers and ifSymbols:
    finalArray = [lowCaseLetters, upperCaseLetters, numbers, symbols]
elif ifNumbers and ifSymbols is False:
    finalArray = [lowCaseLetters, upperCaseLetters, numbers]
elif ifSymbols and ifNumbers is False:
    finalArray = [lowCaseLetters, upperCaseLetters, symbols]
else:
    finalArray = [lowCaseLetters, upperCaseLetters]


def select_random_symbol(x, y, z):
    while len(x) < y:
        for i in range(0, len(z)):
            s = z[i]
            x.append(random.choice(s))


def swap_caracters(arg):
    random.shuffle(arg)
    z = "".join(arg)
    print(z)


select_random_symbol(finalPassword, passwordLenght, finalArray)
swap_caracters(finalPassword)
