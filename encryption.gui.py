from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet
import pyperclip
import ctypes
myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

key = Fernet.generate_key()
fernet = Fernet(key)

def copyAndDes(thing, message):
    pyperclip.copy(message)
    thing.destroy

def messageWindow(title, message):
    win = Toplevel()
    win.title(title)
    win.geometry("750x100")
    win.resizable(False, False)

    img1 = PhotoImage(file="shield.ico")
    win.tk.call('wm', 'iconphoto', win._w, img1)

    Label(win, text=message).pack()
    Button(win, text='Copy', command=copyAndDes(win, str(message))).pack()


def encryptMessage():
    text = textbox.get(1.0, END)

    encrypt = fernet.encrypt(text.encode())
    messageWindow("Encrypt", encrypt.decode())

def decryptMessage():
    message = textbox.get(1.0, END)
    decrypt = fernet.decrypt(message.encode()).decode()
    
    messageWindow("Decrypt", decrypt)

app = Tk()
app.resizable(False, False)
app.title("Encrypt")
app.geometry("500x500")

img = PhotoImage(file="shield.ico")
app.tk.call('wm', 'iconphoto', app._w, img)

textbox = Text(
    app,
    width=100,
    height=5
)

button2 = Button(app, text="Decrypt", width=100, height=3, command=decryptMessage)

button2.pack(side=BOTTOM)

textbox.pack(expand=True)

button1 = Button(app, text="Encrypt", width=100, height=3, command=encryptMessage)

button1.pack(side=BOTTOM)
app.mainloop()
