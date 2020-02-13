from tkinter import *
#heyyyyyyy


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
        else:
            myList.append('/')
    return myList


class Encrypt(Frame):
    def __init__(self, pencere):
        Frame.__init__(self, pencere)
        self.pencere = pencere

        Label(pencere, text="Enter your message: ", relief=GROOVE, width=30).place(x=113, y=30)
        self.Ent1 = Entry(pencere, width=30)
        self.Ent1.place(x=130, y=60)

        Label(pencere, text="Enter key: ", relief=GROOVE, width=30).place(x=113, y=90)
        self.Ent2 = Entry(pencere, width=30)
        self.Ent2.place(x=130, y=120)

        Button(pencere, text="Encrypt", relief=GROOVE, font="bold", command=self.Encrypt).place(x=130, y=150)
        Button(pencere, text="Decrypt", relief=GROOVE, font="bold", command=self.Decrypt).place(x=246, y=150)

        Label(pencere, text="Encrypted/Decrypted Result: ", relief=GROOVE, width=30).place(x=20, y=200)
        self.RESULT = Entry(pencere, width=30)
        self.RESULT.place(x=250, y=200)
        Label(pencere, text="The index points of the ciphertext is: ", relief=GROOVE, width=30).place(x=20, y=230)
        self.RESULTarray = Entry(pencere, width=30)
        self.RESULTarray.place(x=250, y=230)

    def Decrypt(self):
        """
        This function is used to decrypt the given ciphertext using a key & the
        corresponding ciphertext
        Input types: integer, Array of Integers
        Return: Array of Integers

        """
        key = self.Ent2.get()
        key = int(key)
        encr = self.RESULTarray.get()
        finList = []
        encr = encr.split(" ")
        print(encr)
        test = False
        for num in encr:
            if num != '/':
                num = int(num)
                if test:
                    key = key + num
                    test = False
                while num < key:
                    num = num + 27
                num = num - key
                finList.append(int(num))
                key = key + num

            else:
                test = True
        decrypted = ''
        decrypt_list = converter2(finList)
        for last in decrypt_list:  # Loop used to display the decrypted ciphertext
            decrypted += last
        self.RESULT.delete(0, END)
        self.RESULT.insert(0, decrypted)
        self.RESULTarray.delete(0, END)

    def Encrypt(self):

        """
        This method implements the encryption algorithm given to encrypt lowercase
        alphabetic charecters using a key
        Input types: Integer, array of integers
        Return: Array of integers
        """
        conv = self.Ent1.get()
        conv = converter(conv)
        key = self.Ent2.get()
        ciph = []
        print(conv)
        i = 0
        v = int(conv[0]) + int(key)

        for num in conv:
            if num != ' ':
                temp = v % 27
                if temp != 0:
                    ciph.append(temp)

                else:
                    ciph.append(str("/"))
                    v = v + conv[i]
                    temp = v % 27
                    ciph.append(temp)
                i = i + 1
                if i == len(conv):
                    break

                v = v + conv[i]
            else:
                ciph.append(' ')
        encrypted = converter2(ciph)
        final_encrypted = ''
        for some in encrypted:
            final_encrypted += str(some)
        self.RESULTarray.delete(0, END)
        self.RESULTarray.insert(0, ciph)
        self.RESULT.delete(0, END)
        self.RESULT.insert(0, final_encrypted)
        print("The index points of the ciphertext is: ")
        print(ciph)


if __name__ == "__main__":
    root = Tk()
    root.title("Encryption")

    root.resizable(False, False)  # This code helps to disable windows from resizing

    window_height = 300
    window_width = 450

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    Encrypt(root).pack(side="top", fill="both")
    root.mainloop()
