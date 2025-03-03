import os
os.system('cmd /c "pip3 install pycryptodome"')
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from tkinter import *
from tkinter import messagebox
import binascii
from binascii import *

def encrypt():

    screen1=Toplevel(screen)
    screen1.title("Encrypted Message")
    screen1.geometry("400x450")
    screen1.configure(bg="red")

    message = textbox.get('1.0', 'end-1c')
    message = bytes(message, 'utf-8')
#    print(message, "\n")  This line will output plaintext of intended message to encrypt to IDE. Not needed but can be kept.
    
    key = RSA.import_key(open('public_key.pem').read())
    cipher = PKCS1_OAEP.new(key)
    ciphertext = cipher.encrypt(message)
#    print(ciphertext, "\n")  # This line will output Hex Bytes to IDE. Not needed but can be kept.
 
    Label(screen1, text="ENCRYPTED", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
    text2=Text(screen1, font="Rpbote 10", bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text2.place(x=10,y=40,width=380,height=400)

    text2.insert(END, bytes(ciphertext).hex())
#    text2.insert(END, binascii.hexlify(ciphertext).decode('utf-8'))

    
def decrypt():

    screen2=Toplevel(screen)
    screen2.title("Decrypted Message")
    screen2.geometry("400x450")
    screen2.configure(bg="green")

    Label(screen2, text="DECRYPTED", font="calibri", fg="white", bg="green").place(x=10, y=0)
    text3=Text(screen2, font="calibri", bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text3.place(x=10,y=40,width=380,height=400)

    ciphertext=textbox.get('1.0', 'end-1c')
    transform_cipher = bytes(ciphertext, 'utf-8')
#    print(transform_cipher, "\n")     This line will print decoded plaintext to IDE. Not needed but can be kept.
    transform_complete = unhexlify(transform_cipher)
    print(transform_complete, "\n")
    
    key = RSA.import_key(open('private_key.pem').read())
    cipher = PKCS1_OAEP.new(key)
    plaintext = cipher.decrypt(transform_complete)
#    print(plaintext, "\n")       This line will print decoded plaintext to IDE. Not needed but can be kept.
    
    message = plaintext.decode("utf-8")   
    text3.insert(END, message)

def generateKey():
    new_key = RSA.generate(2048)

    private_key = new_key.exportKey("PEM")
    public_key = new_key.publickey().exportKey("PEM")

    fd = open("private_key.pem", "wb")
    fd.write(private_key)
    fd.close()

    fd = open("public_key.pem", "wb")
    fd.write(public_key)
    fd.close()


def main_screen():

    global screen
    global textbox

    
    screen = Tk()
    screen.geometry("500x600")
    screen.title("The Encryptinator")

    def reset():
        textbox.delete(1.0, END)

    
    Label(text="Enter Message", fg="black",
          font=("calibri", 11)).place(x=10,y=10)

    textbox=Text(font="calibri", bg="white", fg="black",relief=GROOVE,
                 wrap=WORD, bd=0)
    textbox.place(x=10, y=30, width=477, height=450)

    

    Button(text="Encrypt", height="2", width=18, bg="red", fg="black",
           bd=0, command=encrypt).place(x=13, y=490)
    Button(text="Decrypt", height="2", width=18, bg="green", fg="black",
           bd=0, command=decrypt).place(x=183, y=490)
    Button(text="Generate Key", height="2", width=18, bg="gray", fg="black",
           bd=0, command=generateKey).place(x=353, y=490)
    Button(text="Reset", height="2", width=45, bg="#1089ff", fg="black",
           bd=0, command=reset).place(x=90, y=540)



    
    screen.mainloop()

main_screen()
