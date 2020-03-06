from string import ascii_letters
from operator import itemgetter
from nltk.corpus import words
from nltk.corpus import wordnet

finalDecryptList = []
finalEncryptList = []
encryptedText = ""
decryptedText = ""
firstRun = 0


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
    MAlist = [[9], [19], [26], [2], [3], [13], [7], [10], [4], [15], [16], [23], [6], [24], [0], [1], [5], [14], [8],
              [11], [20], [21], [22], [25], [12], [17], [18]]  # this is a static mono alphabetic list
    return MAlist


def MonoToNon(monoNumber, MAList):
    """
    This function is used to map the mono alphabetic number to its location in the list
    then it returns that index of where the number is.
    Return : array of integers
    """
    indx = -1
    for x in MAList:  # this is a for loop to iterate over the list
        if x == monoNumber:  # this checks if the the current value is equal to the the current number in the list
            indx += 1  # indicating that we are moving though the list
            return indx  # returning where the number has been found
        else:
            indx += 1  # if we couldn't find the number at that location we move the index


def NoMono():
    NoMAlist = [[i] for i in range(27)]
    return NoMAlist


def Encrypt(text):
    """
    This method implements the encryption algorithm given to encrypt lowercase
    alphabetic charecters using a key
    Input types: Integer, array of integers
    Return: Array of integers
    """
    global MAList
    global encryptedText
    global finalEncryptList
    encryptedText = ""
    index = 2
    NOS = 0  # initializing variables
    NOL = 0
    conv = converter(text)
    if len(finalEncryptList) != 0:
        finalEncryptList = []  # clearing the list if its not empty

    for x in conv:
        if x == " ":
            finalEncryptList.append(" ")  # checking if x is a pace and if it is adding a space the final list
        elif index == 2:
            NOS = x
            index = index - 1
            output = MAList[x]  # checking if index is equal to 2 if it is then we set the number of shifts to x
            str1 = 0
            for last in output:
                str1 += last  # converting from a list to string
            finalEncryptList.append(str1)  # adding the result to the list
        elif index == 1:
            index = index - 1
            NOL = x  # checking if index is equal to 2 if it is then we set the number of letters to shift to x
            output2 = MAList[x]
            str2 = 0
            for last2 in output2:
                str2 += last2  # converting from a list to string
            finalEncryptList.append(str2)  # adding the result to the list
        else:
            if NOL != 0:
                NACC = (x + NOS) % 26
                if NACC == 0:  # checking if the Number After the Caesar Cipher is equal to 0 and then
                    NACC = 26  # setting it to 26
                finalEncryptList.append(NACC)  # appending the final number to the list

                NOL = NOL - 1  # decreasing the number of letter to shift
                if NOL == 0:
                    index = 2

    encryptedList = converter2(finalEncryptList)  # converting the numbers to letters

    for last in encryptedList:  # converting the the list into a string
        encryptedText = encryptedText + last
    return encryptedText


def Decrypt():
    """
    This function is used to decrypt the given ciphertext
    Return: Array of Integers

    """

    global finalDecryptList
    global decryptedText
    global finalEncryptList
    global encryptedText
    global decryptedText
    MAList = Mono()
    decryptedText = ""
    index = 2
    NOS = 0  # initializing variables
    NOL = 0

    if len(finalDecryptList) != 0:
        finalDecryptList = []

    for x in finalEncryptList:
        if x == " ":
            finalDecryptList.append(" ")

        elif index == 2:
            index = index - 1
            output = MonoToNon([x], MAList)  # here we are getting the index of the encrypted letter
            NOS = output  # setting back the number of letters to shift
            finalDecryptList.append(output)
        elif index == 1:
            index = index - 1
            output2 = MonoToNon([x], MAList)
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

    return decryptedText


MAList = Mono()  # running the function and setting it to the variable MAList
encryptedList = []


def letters(text):
    letter_dict = {}
    total = 0
    count = 0
    mostCommonLetters = ""
    p = "%"
    for letter in text:
        if letter in ascii_letters:
            try:
                letter_dict[letter] += 1
            except KeyError:
                letter_dict[letter] = 1

    print("=" * 5, 'Letters', "=" * 5)
    for x in letter_dict.values():
        total += x
    for letter in sorted(letter_dict.items(), key=itemgetter(1), reverse=True):
        if count != 3:
            mostCommonLetters += letter[0]
            count += 1
        x = ((letter[1] / total) * 100)
        print("the %s %.2f%s " % (letter, x, p))
    return mostCommonLetters


def bigrams(text):
    bigram_dict = {}
    bigram_holder = []
    total = 0
    p = "%"
    for letter in text:
        if letter not in ascii_letters:
            bigram_holder = []
            continue
        else:
            bigram_holder.append(letter)

        if len(bigram_holder) == 2:
            bigram = bigram_holder[0] + bigram_holder[1]
            try:
                bigram_dict[bigram] += 1
            except KeyError:
                bigram_dict[bigram] = 1

            last = bigram_holder.pop()
            bigram_holder = []
            bigram_holder.append(last)

    print("=" * 5, 'Bigrams', "=" * 5)
    for x in bigram_dict.values():
        total += x
    for bigram in sorted(bigram_dict.items(), key=itemgetter(1), reverse=True):
        x = ((bigram[1] / total) * 100)
        print("the %s %.2f%s " % (bigram, x, p))


def trigrams(text):
    trigram_dict = {}
    trigram_holder = []
    total = 0
    p = "%"
    for letter in text:
        if letter not in ascii_letters:
            trigram_holder = []
            continue
        else:
            trigram_holder.append(letter)

        if len(trigram_holder) == 3:
            trigram = trigram_holder[0] + trigram_holder[1] + trigram_holder[2]
            try:
                trigram_dict[trigram] += 1
            except KeyError:
                trigram_dict[trigram] = 1

            l1 = trigram_holder.pop()
            l2 = trigram_holder.pop()
            trigram_holder = []
            trigram_holder.append(l2)
            trigram_holder.append(l1)

    print("=" * 5, 'Trigrams', "=" * 5)
    for x in trigram_dict.values():
        total += x
    for trigram in sorted(trigram_dict.items(), key=itemgetter(1), reverse=True):
        x = ((trigram[1] / total) * 100)
        print("the %s %.2f%s " % (trigram, x, p))




def is_english_word(word):
    setofwords = set(words.words())
    setofnetwords = set(wordnet.words())
    if word in setofwords:
        return True
    elif word in setofnetwords:
        return True
    else:
        return False


def CryptoAnaylisis(encryptedTextToAnalize):
    posEncryptedList = 0
    finalCryptoList = []
    monoCryptoList = []
    cryptoCurrentList = []
    posCCList = 0
    monoIndex = 0
    localMAList = NoMono()
    textCryptoCurrent = ""
    textCryptoFinal = ""
    control = 0
    notEcrypted = True
    wordStart = False
    firstWord = True
    CLList = letters(encryptedText)
    encryptedTextConv = converter(encryptedTextToAnalize)
    CCLList = converter(CLList)

    while notEcrypted:
        if posCCList == 0:
            checkNum = CCLList[0] - 5
            for x in encryptedTextConv:
                if control != 2:
                    finalCryptoList.append(x)
                    monoCryptoList.append(x)
                    posEncryptedList += 1
                    control += 1
                elif control == 2:
                    if x == " " and firstWord:
                        finalCryptoList.append(x)
                        posEncryptedList += 1
                        wordStart = True
                        firstWord = False
                    else:
                        if wordStart:
                            if x == " " and firstWord is False:
                                textCryptoCurrentList = converter2(cryptoCurrentList)
                                for last in textCryptoCurrentList:  # converting the the list into a string
                                    textCryptoCurrent += last
                                if is_english_word(textCryptoCurrent):
                                    is_english = "it is a word"
                                else:
                                    is_english = "not a word"

                                print("I think %s is a word and our english dict says its %s but if you think it is "
                                      "then write yes else write no" % (textCryptoCurrent, is_english))
                                userInput = input()
                                if userInput == "yes":
                                    print("great")
                                    cryptoCurrentList.append(x)
                                    finalCryptoList += cryptoCurrentList
                                    localMAList[checkNum] = [monoCryptoList[monoIndex]]
                                    # TODO: replace the mon with the non mon
                                    finalListToPrint = converter2(finalCryptoList)
                                    for last in finalListToPrint:  # converting the the list into a string
                                        textCryptoFinal += last
                                    print("The current final decrypted text is: %s" % textCryptoFinal)
                                    textCryptoCurrent = ""
                                    cryptoCurrentList = []
                                    textCryptoFinal = ""

                                else:
                                    print("shit okay we will reset")
                                    # TODO: Do the Reset part and figure how lol
                                posEncryptedList += 1
                            else:
                                cryptoCurrentList.append(x - checkNum)
                                posEncryptedList += 1

                        else:
                            finalCryptoList.append(x)
        break


testToAnylize = "axe man killed someone while he was a sleep"
encryptedTextToAnalize = Encrypt(testToAnylize)
CryptoAnaylisis(encryptedTextToAnalize)
