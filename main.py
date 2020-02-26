from random import shuffle
from tkinter import *


def Mono():
    """
    This function sets and returns the mono alphabetic list
    Return : array of integers
    """
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
    """
    This function sets and returns the alphabetic list
    Return : array of integers
    """
    NoMAlist = [[i] for i in range(27)]  # returning a list of numbers from 0-26 to resemble the normal alphabetic list
    return NoMAlist  # returning the list


MAList = Mono()  # running the function and setting it to the variable MAList
finalDecryptList = []
finalEncryptList = []  # initializing variables
encryptedList = []


class Encrypt(Frame):
    encryptedText = ""  # initializing variables
    decryptedText = ""

    def __init__(self, pencere):
        """
        This function creates the GUI
        Return : GUI
        """

        Frame.__init__(self, pencere)
        self.pencere = pencere

        Label(pencere, text="Enter text... ", relief=GROOVE, width=25).place(x=60, y=15)
        self.Ent1 = Entry(pencere, width=30)
        self.Ent1.place(x=58, y=50)  # creating the the input box for the text and setting the place

        # creating the buttons and setting their locations
        Button(pencere, text="Encrypt", relief=GROOVE, font="bold", command=self.Encrypt).place(x=30, y=100)
        Button(pencere, text="Decrypt", relief=GROOVE, font="bold", command=self.Decrypt).place(x=190, y=100)

        # creating the output box and setting the location of the box and the size of the box
        Label(pencere, text="The Result: ", relief=GROOVE, width=25).place(x=60, y=160)
        self.Result = Entry(pencere, width=30)
        self.Result.place(x=58, y=190)

        # creating the intial configuration and setting its location and size
        Label(pencere, text="The intial configuration...", relief=GROOVE, width=25).place(x=60, y=240)
        self.initConfig = Text(pencere, width=77)
        self.initConfig.place(x=290, y=15)

    def converter(self, word):
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
            elif x == ' ':  # checking if there is a space
                myList.append(' ')
            else:
                myList.append(int(0))
        return myList

    def converter2(self, dec):
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
            if y == ' ':  # checkin if there is a space
                myList.append(' ')
            elif y in thisdict2:
                myList.append(thisdict2[y])
        return myList

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
        self.Result.config(state=NORMAL)  # enabling edit to the field
        self.initConfig.config(state=NORMAL)  # enabling edit to the field
        self.initConfig.delete(1.0, END)  # clearing the field
        encryptedText = ""
        text = self.Ent1.get()
        index = 2
        NOS = 0  # initializing variables
        NOL = 0
        nIter = 0
        conv = self.converter(text)
        self.initConfig.insert(INSERT, "###############################Encryption############################### \n")
        self.initConfig.insert(INSERT, "We first create the mono alphabetic list \n")
        self.initConfig.insert(INSERT, [["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"], ["h"], ["i"], ["j"], ["k"],
                                        ["l"], ["m"], ["n"], ["o"], ["p"], ["q"], ["r"], ["s"], ["t"], ["u"], ["v"],
                                        ["w"], ["x"], ["y"], ["z"]])
        self.initConfig.insert(INSERT, "\n")
        self.initConfig.insert(INSERT, [["|"], ["|"], ["|"], ["|"], ["|"], ["|"], ["|"], ["|"], ["|"], ["|"], ["|"],
                                        ["|"], ["|"], ["|"], ["|"], ["|"], ["|"], ["|"], ["|"], ["|"], ["|"], ["|"],
                                        ["|"], ["|"], ["|"], ["|"]])
        self.initConfig.insert(INSERT, "\n")
        self.initConfig.insert(INSERT, [["i"], ["s"], ["z"], ["b"], ["c"], ["m"], ["g"], ["j"], ["d"], ["o"], ["p"],
                                        ["w"], ["f"], ["x"], ["a"], ["e"], ["n"], ["h"], ["k"], ["t"], ["u"], ["v"],
                                        ["y"], ["l"], ["q"], ["r"]])
        self.initConfig.insert(INSERT, "\n")
        self.initConfig.insert(INSERT, "We then take the input and convert it to numbers and add them to a list \n")
        self.initConfig.insert(INSERT, conv)
        self.initConfig.insert(INSERT, "\n")

        if len(finalEncryptList) != 0:
            finalEncryptList = []  # clearing the list if its not empty

        for x in conv:
            if x == " ":
                finalEncryptList.append(" ")  # checking if x is a pace and if it is adding a space the final list
            elif index == 2:
                NOS = x
                index = index - 1
                nIter = nIter + 1
                output = MAList[x]  # checking if index is equal to 2 if it is then we set the number of shifts to x
                str1 = 0
                for last in output:
                    str1 += last  # converting from a list to string
                finalEncryptList.append(str1)  # adding the result to the list
                self.initConfig.insert(INSERT, "Here we set the Number of Shifts to %d\n" % (int(x)))
            elif index == 1:
                index = index - 1
                nIter = nIter + 1
                NOL = x  # checking if index is equal to 2 if it is then we set the number of letters to shift to x
                output2 = MAList[x]
                str2 = 0
                for last2 in output2:
                    str2 += last2  # converting from a list to string
                finalEncryptList.append(str2)  # adding the result to the list
                self.initConfig.insert(INSERT, "Here we set the Number of Letter to do the shift to %d\n" % (int(x)))
            else:
                if NOL != 0:
                    NACC = (x + NOS) % 26
                    if NACC == 0:  # checking if the Number After the Caesar Cipher is equal to 0 and then
                        NACC = 26  # setting it to 26
                    finalEncryptList.append(NACC)  # appending the final number to the list
                    self.initConfig.insert(INSERT, "Now we do the caesar cipher to %d\n" % (int(x)))
                    self.initConfig.insert(INSERT, "the result of the caesar cipher is %d\n" % (int(NACC)))
                    NOL = NOL - 1  # decreasing the number of letter to shift
                    if NOL == 0:
                        index = 2
        self.initConfig.insert(INSERT, "the result of the encryption in a list format is \n")
        self.initConfig.insert(INSERT, finalEncryptList)
        self.initConfig.insert(INSERT, "\n")
        encryptedList = self.converter2(finalEncryptList)  # converting the numbers to letters
        self.initConfig.insert(INSERT, "we now convert the numbers back to letters and the result is \n")
        self.initConfig.insert(INSERT, encryptedList)
        self.initConfig.insert(INSERT, "\n")
        for last in encryptedList:  # converting the the list into a string
            encryptedText = encryptedText + last
        self.initConfig.insert(INSERT, "the final result of the encryption a text format is: ")
        self.initConfig.insert(INSERT, encryptedText)
        self.Result.delete(0, END)
        self.Result.insert(0, encryptedText)
        self.Result.config(state=DISABLED)
        self.initConfig.config(state=DISABLED)
        encryptedText = ""  # setting the encrypted text back to an empty string

    def Decrypt(self):
        """
        This function is used to decrypt the given ciphertext
        Return: Array of Integers

        """

        global finalDecryptList
        global decryptedText
        global finalEncryptList
        global encryptedText
        global decryptedText
        global MAList
        decryptedText = ""
        self.Result.config(state=NORMAL)
        self.initConfig.config(state=NORMAL)
        self.initConfig.delete(1.0, END)
        index = 2
        NOS = 0  # initializing variables
        NOL = 0
        self.initConfig.insert(INSERT, "###############################Decryption############################### \n")
        self.initConfig.insert(INSERT, "We first create the alphabetic list \n")
        self.initConfig.insert(INSERT, [["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"], ["h"], ["i"], ["j"], ["k"],
                                        ["l"], ["m"], ["n"], ["o"], ["p"], ["q"], ["r"], ["s"], ["t"], ["u"], ["v"],
                                        ["w"], ["x"], ["y"], ["z"]])
        self.initConfig.insert(INSERT, "\n")
        self.initConfig.insert(INSERT, [["|"], ["|"], ["|"], ["|"], ["|"], ["|"], ["|"], ["|"], ["|"], ["|"], ["|"],
                                        ["|"], ["|"], ["|"], ["|"], ["|"], ["|"], ["|"], ["|"], ["|"], ["|"], ["|"],
                                        ["|"], ["|"], ["|"], ["|"]])
        self.initConfig.insert(INSERT, "\n")
        self.initConfig.insert(INSERT, [["i"], ["s"], ["z"], ["b"], ["c"], ["m"], ["g"], ["j"], ["d"], ["o"], ["p"],
                                        ["w"], ["f"], ["x"], ["a"], ["e"], ["n"], ["h"], ["k"], ["t"], ["u"], ["v"],
                                        ["y"], ["l"], ["q"], ["r"]])
        self.initConfig.insert(INSERT, "\n")
        self.initConfig.insert(INSERT, "We then take the encrypted list of numbers and add them to a list \n")
        self.initConfig.insert(INSERT, finalEncryptList)
        self.initConfig.insert(INSERT, "\n")

        if len(finalDecryptList) != 0:
            finalDecryptList = []

        for x in finalEncryptList:
            if x == " ":
                finalDecryptList.append(" ")

            elif index == 2:
                index = index - 1
                output = MonoToNon([x], MAList)  # here we are getting the index of the encrypted letter
                self.initConfig.insert(INSERT, "Now we map the encrypted letter with the unencrypted list\n")
                NOS = output  # setting back the number of letters to shift
                self.initConfig.insert(INSERT, "In this case the %d maps to %d which is the Number of shifts"
                                               "\n" % (int(x), int(NOS)))
                finalDecryptList.append(output)
            elif index == 1:
                index = index - 1
                self.initConfig.insert(INSERT, "Now we map the encrypted letter with the unencrypted list\n")
                output2 = MonoToNon([x], MAList)
                NOL = output2
                self.initConfig.insert(INSERT, "In this case the %d maps to %d which is the number of letter to "
                                               "shift \n" % (int(x), int(NOS)))
                finalDecryptList.append(output2)
            else:
                if NOL != 0:
                    self.initConfig.insert(INSERT, "now we are deciphering caesar cipher number\n")
                    NACC = (x - NOS) % 26
                    if NACC == 0:
                        NACC = 26
                    self.initConfig.insert(INSERT, "%d deciphered to %d\n" % (int(x), int(NACC)))
                    finalDecryptList.append(NACC)
                    NOL = NOL - 1
                    if NOL == 0:
                        index = 2
        self.initConfig.insert(INSERT, "the result of the decryption in a list format is \n")
        self.initConfig.insert(INSERT, finalDecryptList)
        self.initConfig.insert(INSERT, "\n")
        DecryptList = self.converter2(finalDecryptList)
        self.initConfig.insert(INSERT, "we now convert the numbers back to letters and the result is \n")
        self.initConfig.insert(INSERT, DecryptList)
        self.initConfig.insert(INSERT, "\n")
        for last in DecryptList:
            decryptedText = decryptedText + last
        self.initConfig.insert(INSERT, "the final result of the decryption a text format is: ")
        self.initConfig.insert(INSERT, decryptedText)
        self.Result.delete(0, END)
        self.Result.insert(0, decryptedText)
        self.Result.config(state=DISABLED)
        self.initConfig.config(state=DISABLED)
        decryptedText = ""
        finalEncryptList = []
        finalDecryptList = []


if __name__ == "__main__":
    root = Tk()
    root.title("Monosar")
    root.iconbitmap(r'favicon.ico')

    # root.resizable(False, False)  # This code helps to disable windows from resizing

    window_height = 420
    window_width = 950

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    Encrypt(root).pack(side="top", fill="both")
    root.mainloop()
