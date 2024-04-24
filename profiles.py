def createProfile(email, bio, pfp):
    profiles = open("profiles.txt", "a")
    profiles.write(email + "|" + bio + "|" + pfp + "\n")
    profiles.close()

def updateFirstName(email, first):
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
                info[0] + "|" + info[1] + "|" + info[2] + "|" + first + "|" + info[4] + "|" + info[5] + "\n")
        else:
            userFile.write(user + "\n")
        user = users[i]
    userFile.close()


def updateLastName(email, last):
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
                info[0] + "|" + info[1] + "|" + info[2] + "|" + info[3] + "|" + last + "|" + info[5] + "\n")
        else:
            userFile.write(user + "\n")
        user = users[i]
    userFile.close()


def updateAddress(email, addy):
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
                info[0] + "|" + info[1] + "|" + info[2] + "|" + info[3] + "|" + info[4] + "|" + addy + "\n")
        else:
            userFile.write(user + "\n")
        user = users[i]
    userFile.close()


def updateBio(email, bio):
    profileFile = open("profiles.txt", "r")
    users = profileFile.read().split("\n")
    profileFile.close()
    profileFile = open("profiles.txt", "w")
    i = 0
    user = users[i]
    while user != "":
        i += 1
        info = user.split('|')
        if info[0] == email:
            profileFile.write(
                info[0] + "|" + bio + "|" + info[2] + "\n")
        else:
            profileFile.write(user + "\n")
        user = users[i]
    profileFile.close()


def updatePFP(email, pfp):
    profileFile = open("profiles.txt", "r")
    users = profileFile.read().split("\n")
    profileFile.close()
    profileFile = open("profiles.txt", "w")
    i = 0
    user = users[i]
    while user != "":
        i += 1
        info = user.split('|')
        if info[0] == email:
            profileFile.write(
                info[0] + "|" + info[1] + "|" + pfp + "\n")
        else:
            profileFile.write(user + "\n")
        user = users[i]
    profileFile.close()

def update(email, update):
    userFile = open("users.txt", "r")
    users = userFile.read().split("\n")
    userFile.close()
    userFile = open("users.txt", "w")
    i = 0
    user = users[i]
    ret = False
    while user != "":
        i += 1
        info = user.split('|')
        if info[0] == email:
            userFile.write(
                info[0] + "|" + info[1] + "|" + info[2] + "|" + update.get('firstName') + "|" + update.get('lastName') + "|" + update.get('state') + "\n")
            ret = not ret
            break
        else:
            userFile.write(user + "\n")
        user = users[i]
    userFile.close()
    profileFile = open("profiles.txt", "r")
    users = profileFile.read().split("\n")
    profileFile.close()
    profileFile = open("profiles.txt", "w")
    i = 0
    user = users[i]
    while user != "":
        i += 1
        info = user.split('|')
        if info[0] == email:
            profileFile.write(
                info[0] + "|" + update.get('bio') + "|" + update.get('pfp') + "\n")
            ret = ret and True
            break
        else:
            profileFile.write(user + "\n")
        user = users[i]
    profileFile.close()
    return ret

def getPFP(email):
    profiles = open("profiles.txt", "r")
    users = profiles.read().split("\n")
    profiles.close()
    i = 0
    user = users[i]
    while user != "":
        i += 1
        info = user.split("|")
        if info[0] == email:
            return info[2]
        else:
            user = users[i]
    return "picture not found"


def getBio(email):
    profiles = open("profiles.txt", "r")
    users = profiles.read().split("\n")
    profiles.close()
    i = 0
    user = users[i]
    while user != "":
        i += 1
        info = user.split("|")
        if info[0] == email:
            return info[1]
        else:
            user = users[i]
    return "bio not found"


def getName(email):
    usersFile = open("users.txt", "r")
    users = usersFile.read().split("\n")
    usersFile.close()
    i = 0
    user = users[i]
    while user != "":
        i += 1
        info = user.split("|")
        if info[0] == email:
            return info[3] +" "+ info[4]
        else:
            user = users[i]

    usersFile = open("charities.txt", "r")
    users = usersFile.read().split("\n")
    usersFile.close()
    i = 0
    user = users[i]
    while user != "":
        i += 1
        info = user.split(",")
        if info[1] == email:
            return info[0]
        else:
            user = users[i]
    return "name not found"


def getAddress(email):
    usersFile = open("users.txt", "r")
    users = usersFile.read().split("\n")
    usersFile.close()
    i = 0
    user = users[i]
    while user != "":
        i += 1
        info = user.split("|")
        if info[0] == email:
            return info[5]
        else:
            user = users[i]
    return "address not found"


# wasn't sure exactly how you'd want the info so made this just in case, returns list {name, address, bio, pfp}
def getEntireProfile(email):
    usersFile = open("users.txt", "r")
    users = usersFile.read().split("\n")
    usersFile.close()
    i = 0
    output = []
    user = users[i]
    while user != "":
        i += 1
        info = user.split("|")
        if info[0] == email:
            output = [info[3], info[4], info[5]]
            break
        else:
            user = users[i]

    profiles = open("profiles.txt", "r")
    users = profiles.read().split("\n")
    profiles.close()
    i = 0
    user = users[i]
    while user != "":
        i += 1
        info = user.split("|")
        if info[0] == email:
            output.append(info[1])
            output.append(info[2])
            break
        else:
            user = users[i]
    if len(output) == 0:
        return "no info found"
    else:
        return output

