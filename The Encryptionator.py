import os

# Installs the 'pycryptodome' package using pip (needed for RSA encryption/decryption)
os.system('cmd /c "pip3 install pycryptodome"')

# Imports necessary cryptographic modules for RSA encryption and decryption
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

# Imports GUI-related modules from tkinter
from tkinter import *
from tkinter import messagebox

# Imports binascii for binary-to-hex conversions
import binascii
from binascii import *

# Function to encrypt a message
def encrypt():
    # Creates a new window for displaying the encrypted message
    screen1 = Toplevel(screen)
    screen1.title("Encrypted Message")
    screen1.geometry("400x450")
    screen1.configure(bg="red")

    # Retrieves message from the textbox and encodes it to bytes
    message = textbox.get('1.0', 'end-1c')
    message = bytes(message, 'utf-8')

    # Imports the public key from a file
    key = RSA.import_key(open('public_key.pem').read())

    # Creates a cipher object using RSA with OAEP padding
    cipher = PKCS1_OAEP.new(key)

    # Encrypts the message using the public key
    ciphertext = cipher.encrypt(message)

    # Creates a label for the encrypted message display
    Label(screen1, text="ENCRYPTED", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)

    # Creates a text box to display the encrypted message
    text2 = Text(screen1, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text2.place(x=10, y=40, width=380, height=400)

    # Inserts the encrypted message as a hex string into the textbox
    text2.insert(END, bytes(ciphertext).hex())

# Function to decrypt a message
def decrypt():
    # Creates a new window for displaying the decrypted message
    screen2 = Toplevel(screen)
    screen2.title("Decrypted Message")
    screen2.geometry("400x450")
    screen2.configure(bg="green")

    # Creates a label for the decrypted message display
    Label(screen2, text="DECRYPTED", font="calibri", fg="white", bg="green").place(x=10, y=0)

    # Creates a text box to display the decrypted message
    text3 = Text(screen2, font="calibri", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text3.place(x=10, y=40, width=380, height=400)

    # Retrieves the ciphertext from the textbox
    ciphertext = textbox.get('1.0', 'end-1c')

    # Converts the hex string back into bytes
    transform_cipher = bytes(ciphertext, 'utf-8')
    transform_complete = unhexlify(transform_cipher)

    # Imports the private key from a file
    key = RSA.import_key(open('private_key.pem').read())

    # Creates a cipher object using RSA with OAEP padding
    cipher = PKCS1_OAEP.new(key)

    # Decrypts the message using the private key
    plaintext = cipher.decrypt(transform_complete)

    # Decodes the plaintext from bytes to a string
    message = plaintext.decode("utf-8")

    # Inserts the decrypted message into the textbox
    text3.insert(END, message)

# Function to generate a new RSA key pair
def generateKey():
    # Generates a new 2048-bit RSA key
    new_key = RSA.generate(2048)

    # Exports the private key in PEM format
    private_key = new_key.exportKey("PEM")

    # Exports the corresponding public key in PEM format
    public_key = new_key.publickey().exportKey("PEM")

    # Saves the private key to a file
    fd = open("private_key.pem", "wb")
    fd.write(private_key)
    fd.close()

    # Saves the public key to a file
    fd = open("public_key.pem", "wb")
    fd.write(public_key)
    fd.close()

# Function to create the main application window
def main_screen():
    # Declares global variables for the main screen and textbox
    global screen
    global textbox

    # Initializes the main application window
    screen = Tk()
    screen.geometry("500x600")
    screen.title("The Encryptinator")

    # Function to clear the textbox
    def reset():
        textbox.delete(1.0, END)

    # Creates a label for the input field
    Label(text="Enter Message", fg="black", font=("calibri", 11)).place(x=10, y=10)

    # Creates a textbox for entering messages
    textbox = Text(font="calibri", bg="white", fg="black", relief=GROOVE, wrap=WORD, bd=0)
    textbox.place(x=10, y=30, width=477, height=450)

    # Creates buttons for encryption, decryption, key generation, and reset
    Button(text="Encrypt", height="2", width=18, bg="red", fg="black",
           bd=0, command=encrypt).place(x=13, y=490)
    Button(text="Decrypt", height="2", width=18, bg="green", fg="black",
           bd=0, command=decrypt).place(x=183, y=490)
    Button(text="Generate Key", height="2", width=18, bg="gray", fg="black",
           bd=0, command=generateKey).place(x=353, y=490)
    Button(text="Reset", height="2", width=45, bg="#1089ff", fg="black",
           bd=0, command=reset).place(x=90, y=540)

    # Runs the main event loop
    screen.mainloop()

# Calls the main function to start the application
main_screen()
