import re, nltk
from nltk.corpus import wordnet as wn

emailReg = r'[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}'
specChar = r'[.!@#$%^&*()\-=_+/?<>`~\[\]]'
capLetter = r'[A-Z]'
lengthReq = r'.{12,}'
phoneReq = r'^[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$'


def emailValid(email):
    if not re.fullmatch(emailReg, email):
        return False
    else:
        return True

def passValid(password):
    if not re.search(specChar, password) or not re.search(capLetter, password) or not re.search(lengthReq, password):
        return False
    else:
        return True

def phoneValid(phoneNum):
    if not re.match(phoneReq, phoneNum):
        return False
    else:
        return True

def charity_register(name, email, password, phoneNumber, address, charityType, charityBio):

    if not passValid(password):
        return -1

    if not phoneValid(phoneNumber):
        return -2

    charities = open("charities.txt", "r")
    charity = charities.readline()
    while charity != "":
        info = charity.split(',')
        if info[1] == email:
            return -3
        else:
            charity = charities.readline()
    charities.close()

    charities = open("charities.txt", "a")
    charities.write(name + "," + email + "," + password + "," + phoneNumber + "," + address + "," + charityType + "," + charityBio + "\n")
    charities.close()
    return 1

def getKeywords(text):
    tokens = nltk.pos_tag(nltk.word_tokenize(text.lower()))
    ret = []
    for token in tokens:
        if token[1]=='CD'or token[1]=='MD'or token[1]=='DT'or token[1]=='IN':
            tokens.remove(token)
        else:
            ret.append(token[0])
    return ret

def areSyn(word1, word2):
    syn = wn.synonyms(word1)
    ret = False
    if(not syn==[]):
        for i in syn:
            if word2 in i:
                ret = True
    return ret


def charity_search(text):
    charities = open("charities.txt", "r")
    charity = charities.readline()
    charitySims = {}
    if(text==None):
        return charitySims
    keywords = getKeywords(text)
    while charity != "":
        info = charity.split(',')
        if info[0].lower() == text.lower():
            charitySims[info[0]] = 100
        else:
            charitySims[info[0]] = 0
            if info[5].lower() in keywords:
                charitySims[info[0]] = 50
            l = len(keywords)
            for word in keywords:
                if word in info[6].lower():
                    charitySims[info[0]] = charitySims[info[0]] + 50*(1/l)
                else:
                    for s in getKeywords(info[6]):
                        if areSyn(word,s) or areSyn(s,word):
                            charitySims[info[0]] = charitySims[info[0]] + 50*(1/l)
            charity = charities.readline()
    charities.close()
    ch = []
    for charity in charitySims:
        if not charitySims[charity]==0:
            ch.append(str(charitySims[charity])+"|"+charity)
    ch.sort()
    ch1 = []
    for c in ch:
        ch1.append(c.split('|')[1])
    ret = {}
    keywords = getKeywords(text)
    for name in ch1:
        charities = open("charities.txt", "r")
        charity = charities.readline()
        while charity != "":
            info = charity.split(',')
            if info[0].lower() == name.lower():
                ret[info[0]] = {'email':info[1],'phone':info[3],'addr':info[4],'orgType':info[5],'bio':info[6]}
            charity = charities.readline()
    charities.close()
    
    return ret

