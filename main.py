from random import shuffle
from tkinter import *


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


def MonoToNon(monoNumber, MAList):
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


MAList = Mono()
finalDecryptList = []
finalEncryptList = []
encryptedList = []

class Encrypt(Frame):

    encryptedText = ""
    decryptedText = ""

    def __init__(self, pencere):
        Frame.__init__(self, pencere)
        self.pencere = pencere

        Label(pencere, text="Enter text... ", relief=GROOVE, width=25).place(x=210, y=15)
        self.Ent1 = Entry(pencere, width=30)
        self.Ent1.place(x=208, y=50)

        Button(pencere, text="Encrypt", relief=GROOVE, font="bold", command=self.Encrypt).place(x=180, y=100)
        Button(pencere, text="Decrypt", relief=GROOVE, font="bold", command=self.Decrypt).place(x=340, y=100)

        Label(pencere, text="The intial configuration...", relief=GROOVE, width=25).place(x=210, y=240)

        Label(pencere, text="The Result: ", relief=GROOVE, width=25).place(x=210, y=160)
        self.RESULTExplain = Text(pencere, width=77)
        self.RESULTExplain.place(x=20, y=290)
        self.Result = Entry(pencere, width=30)
        self.Result.place(x=208, y=190)


    def Decrypt(self):
        """
        This function is used to decrypt the given ciphertext using a key & the
        corresponding ciphertext
        Input types: integer, Array of Integers
        Return: Array of Integers

        """

        global finalDecryptList
        global decryptedText
        global finalEncryptList
        global encryptedText
        global decryptedText
        global MAList

        index = 2
        NOS = 0
        NOL = 0
        for x in finalEncryptList:
            if index == 2:
                index = index - 1
                output = MonoToNon([x], MAList)
                NOS = output
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

        self.Result.delete(0, END)
        self.Result.insert(0, decryptedText)

    def Encrypt(self):

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
        text = self.Ent1.get()
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
        encryptedList = converter2(finalEncryptList)
        for last in encryptedList:
            encryptedText = encryptedText + last
        self.Result.delete(0, END)
        self.Result.insert(0, encryptedText)


if __name__ == "__main__":
    root = Tk()
    root.title("Monosar")

    # root.resizable(False, False)  # This code helps to disable windows from resizing

    window_height = 600
    window_width = 660

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    Encrypt(root).pack(side="top", fill="both")
    root.mainloop()
