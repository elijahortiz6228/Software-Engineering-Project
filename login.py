import re

emailReg = r'[A-Za-z0-9._+-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,7}'
specChar = r'[.!@#$%^&*()\-=_+/?<>`~\[\]]'
capLetter = r'[A-Z]'
lengthReq = r'.{12,}'


def emailValid(email):
    if not re.fullmatch(emailReg, email):
        return False
    return True


def passValid(password):
    if not re.search(specChar, password) or not re.search(capLetter, password) or not re.search(lengthReq, password):
        return False
    return True


def login(email, password):
    # check if user id and password are in users file
    users = open(r"users.txt")
    user = users.readline()
    while user != "":
        info = user.split('|')
        if info[0] == email:
            if info[1] == password:
                return True
            else:
                return False
        else:
            user = users.readline()
    users.close()
    charities = open(r"charities.txt")
    charity = charities.readline()
    while charity != "":
        charity_info = charity.split(',')
        if charity_info[1] == email:
            if charity_info[2] == password:
                return True
            else:
                return False
        else:
            charity = charities.readline()

    charities.close()
    return False

def charity(email):
    # check if user id and password are in users file
    users = open(r"users.txt")
    user = users.readline()
    while user != "":
        info = user.split('|')
        if info[0] == email:
            return False
        else:
            user = users.readline()
    users.close()
    charities = open(r"charities.txt")
    charity = charities.readline()
    while charity != "":
        charity_info = charity.split(',')
        if charity_info[1] == email:
            return True
        else:
            charity = charities.readline()

    charities.close()
    return False

def register(email, password, security, first, last, state):

    # check if password is valid - capital letter, special character, 12+ length
    if not passValid(password):
        return -2

    # check if email already taken
    users = open("users.txt", "r")
    user = users.readline()
    while user != "":
        info = user.split('|')
        if info[0] == email:
            return -3
        else:
            user = users.readline()
    users.close()

    # if it doesn't already exist, add to file
    users = open("users.txt", "a")
    users.write(email + "|" + password + "|" + security + "|" + first + "|" + last + "|" + state + "\n")
    users.close()
    return 1


def forgotPasswordEmail(email):
    # just checks if the email exists
    users = open("users.txt", "r")
    user = users.readline()
    while user != "":
        info = user.split('|')
        if info[0] == email:
            return True
        else:
            user = users.readline()
    users.close()
    return False


def forgotPassword(email, answer):
    # check that the email exists, and if it does, check if security question answer matches
    users = open("users.txt", "r")
    user = users.readline()
    while user != "":
        info = user.split('|')
        if info[0] == email:
            if info[2] == answer:
                return True
            return False
        else:
            user = users.readline()
    users.close()
    return False


def resetPassword(email, newPassword):
    # only use this if forgotPassword returns true
    userFile = open("users.txt", "r")
    users = userFile.read().split("\n")
    userFile.close()
    userFile = open("users.txt", "w")
    i = 0
    user = users[i]
    while user != "":
        i += 1
        info = user.split('|')
        if info[0] == email:
            userFile.write(
                info[0] + "|" + newPassword + "|" + info[2] + "|" + info[3] + "|" + info[4] + "|" + info[5] + "\n")
        else:
            userFile.write(user + "\n")
        user = users[i]
    userFile.close()

