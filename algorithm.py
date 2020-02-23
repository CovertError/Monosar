from random import shuffle

finalDecryptList = []
finalEncryptList = []
encryptedText = ""
decryptedText = ""


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
        "1": "a",
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
    MAlist = [[i] for i in range(27)]
    MAlist.pop(0)
    shuffle(MAlist)
    return MAlist


def MonoToNon(monoNumber):
    indx = -1
    for x in MAList:
        if x == monoNumber:
            indx += 1
            return indx
        else:
            indx += 1

def NoMono():
    NoMAlist = [[i] for i in range(27)]
    NoMAlist.pop(0)
    return NoMAlist


def Encrypt():
    global encryptedText
    text = "helloamigoimyusra"
    index = 2
    NOS = 0
    NOL = 0
    nIter = 0
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
            finalEncryptList.append(str1)
        elif index == 1:
            index = index - 1
            nIter = nIter + 1
            NOL = x
            output2 = MAList[x]
            str2 = 0
            for last2 in output2:
                str2 += last2
            finalEncryptList.append(str2)
        else:
            if NOL != 0:
                NACC = (x + NOS) % 26
                if NACC == 0:
                    NACC = 26
                finalEncryptList.append(NACC)
                NOL = NOL - 1
                if NOL == 0:
                    index = 2
    NoMono()
    encryptedList = converter2(finalEncryptList)
    for last in encryptedList:
        encryptedText = encryptedText + last
    print("This is the encrypted Text: " + encryptedText)


def Decrypt():
    global decryptedText
    index = 2
    NOS = 0
    NOL = 0
    for x in finalEncryptList:
        if index == 2:
            index = index - 1
            output = MonoToNon([x])
            NOS = output
            finalDecryptList.append(output)
        elif index == 1:
            index = index - 1
            output2 = MonoToNon([x])
            NOL = output2
            finalDecryptList.append(output2)
        else:
            if NOL != 0:
                NACC = (x - NOS) % 26
                if NACC == 0:
                    NACC = 26
                finalDecryptList.append(NACC)
                NOL = NOL - 1
                if NOL == 0:
                    index = 2
    DecryptList = converter2(finalDecryptList)
    for last in DecryptList:
        decryptedText = decryptedText + last

    print("This is the decrypted Text: " + decryptedText)


MAList = Mono()
Encrypt()
Decrypt()
