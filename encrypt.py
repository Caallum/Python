import sys
import random

letters = {
    "a": "001",
    "b": "011",
    "c": "111",
    "d": "0001",
    "e": "0011",
    "f": "0111",
    "g": "1111",
    "h": "00001",
    "i": "00011",
    "j": "00111",
    "k": "01111",
    "l": "11111",
    "m": "000001",
    "n": "000011",
    "o": "000111",
    "p": "001111",
    "q": "011111",
    "r": "111111",
    "s": "0000001",
    "t": "0000011",
    "u": "0000111",
    "v": "0001111",
    "w": "0011111",
    "x": "0111111",
    "y": "1111111",
    "z": "0000000",
    " ": "00000000"
}

reverseLetters = {
    "001": "a",
    "011": "b",
    "111": "c",
    "0001": "d",
    "0011": "e",
    "0111": "f",
    "1111": "g",
    "00001": "h",
    "00011": "i",
    "00111": "j",
    "01111": "k",
    "11111": "l",
    "000001": "m",
    "000011": "n",
    "000111": "o",
    "001111": "p",
    "011111": "q",
    "111111": "r",
    "0000001": "s",
    "0000011": "t",
    "0000111": "u",
    "0001111": "v",
    "0011111": "w",
    "0111111": "x",
    "1111111": "y",
    "0000000": "z",
    "00000000": " "
}

class encryptMessage:
    def __init__(self, Message):
        code = ""
        hash = self.generateHash(5)
        for x in range(0, len(Message)):
            char = Message[x].lower()
            code = code + str(letters[char]) + " "
        print(hash + code)
    
    def generateHash(self, Len):
        chars = ["0", "1"]
        hash = ""
        for x in range(0, int(Len)):
            hash = hash + random.choice(chars)
        
        return hash + " "

class decryptMessage:
    def __init__(self, encryptedMessage):
        decryptedCode = ""
        sections = str(encryptedMessage).split(" ")
        for x in range(1, len(sections)):
            section = sections[x]

            if section not in reverseLetters: continue

            decryptedCode = decryptedCode + str(reverseLetters[section])
        print(decryptedCode)


choice = input("Encrypt or decrypt a message: (e/d) ")
if choice == 'e':
    string = input("Please enter a string to encrypt: ")
    encryptMessage(string)
elif choice == 'd':
    code = input("Please enter a code to decrypt: ")
    decryptMessage(code)
