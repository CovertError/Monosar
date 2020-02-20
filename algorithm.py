import random
from random import shuffle


def converter(word):
    """
    This method is used to covert alphabetic charecters into the required index
    for encryption and decryption
    input types: array of string
    Return : array of integers
    """
    thisdict = {
        "a": "1",
        "b": "2", "c": "3", "d": "4", "e": "5", "f": "6", "g": "7", "h": "8", "i": "9",
        "j": "10", "k": "11", "l": "12", "m": "13", "n": "14", "o": "15", "p": "16",
        "q": "17", "r": "18", "s": "19", "t": "20", "u": "21", "v": "22", "w": "23",
        "x": "24", "y": "25", "z": "26"
    }
    myList = []
    for x in word:
        if x in thisdict:
            myList.append(int(thisdict[x]))
        elif x == ' ':
            myList.append(' ')
        else:
            myList.append(int(0))
    return myList


def converter2(dec):
    """
    This method is used to covert index numbers back into their alphabetic value
    for encryption and decryption
    input types: array of integers
    output types: array of strings
    """
    thisdict2 = {
        "0": "a",
        "2": "b", "3": "c", "4": "d", "5": "e", "6": "f", "7": "g", "8": "h", "9": "i",
        "10": "j", "11": "k", "12": "l", "13": "m", "14": "n", "15": "o", "16": "p",
        "17": "q", "18": "r", "19": "s", "20": "t", "21": "u", "22": "v", "23": "w",
        "24": "x", "25": "y", "26": "z"
    }
    temp = []
    myList = []
    for x in dec:
        temp.append(str(x))
    for y in temp:
        if y == ' ':
            myList.append(' ')
        elif y in thisdict2:
            myList.append(thisdict2[y])
    return myList

def Mono():
    MAlist = [[i] for i in range(25)]
    shuffle(MAlist)
    print(MAlist)
    return MAlist

def Encrypt():
    text = "hello"
    index = 2
    MAList = Mono()
    NOS = 0
    NOL = 0
    finalList = []
    NACC = 0
    nIter = 0
    output = 0

    conv = converter(text)

    for x in conv:
        if index == 2:
            NOS = x
            index = index - 1
            nIter = nIter + 1
            output = MAList[x]
            str1 = 0
            for last in output:
                str1 += last
            finalList.append(str1)
        elif index == 1:
            index = index - 1
            nIter = nIter + 1
            NOL = x
            str2 = 0
            for last in output:
                str2 += last
            finalList.append(str2)
        else:
            if NOL != 0:
                NACC = (x + NOS) % 26
                finalList.append(NACC)
            else:
                index = 2

    print(finalList)
    print(converter2(finalList))


Encrypt()





