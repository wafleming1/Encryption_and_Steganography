<h1>Encryption and Network Steganography</h1>

 ### [YouTube Demonstration](https://youtu.be/wIjI5Vcx7C4) <br/>

🔑 Security Note <br/>
This tool demonstrates basic use of PKI and encryption and should not be used for highly sensitive data or production systems.

<h2>Features</h2>

- <b> Generate RSA Key Pairs (2048-bit). <br/>
- <b> Encrypt Messages using the public key and decrypts messages using the private key to retrieve the original plaintext. <br/>
- <b> User-Friendly Interface with a Tkinter-based GUI for easy encryption/decryption. <br/>



<h2>Description</h2>

- A simple GUI-based encryption and decryption tool using RSA public-key cryptography.<br/><br/>

<p align="center">
How It Works Step by Step <br/> <br/>
Clicking Generate Key: <br/>
Creates a key pair for encryption and decryption. The keys must be generated first prior to any encryption and decryption operations. <br/><br/>
1. User types a message into the text box. <br/><br/>
Main UI <br/>
<img src="https://i.imgur.com/TBAjI2l.png" height="50%" width="50%"/> <br/> <br/> <br/>
2. Clicking Encrypt: <br/> <br/>
The program encrypts the message using the public key and displays it in a new window. <br/> <br/>
Encrypted Window <br/>
<img src="https://i.imgur.com/F3n5MhF.png" height="50%" width="50%"/> <br/> 
NOTE - Ecrypted output must be copied and pasted back into the Main UI for decrypting.<br/> <br/> <br/>
3. Clicking Decrypt: <br/><br/>
The program reads the encrypted message and decrypts it using the private key and the decrypted message is displayed. <br/><br/>
<img src="https://i.imgur.com/iraVXRo.png" height="50%" width="50%"/> <br/> <br/> <br/>
Clicking Generate Key: <br/>
Creates a key pair for encryption and decryption. The keys must be generated first prior to any encryption and decryption operations.<br/>
</p>

<h2>Languages and Utilities Used</h2>

- Python
- [Scapy](https://scapy.net/)
- [Wireshark](https://www.wireshark.org/)


<h2>Environments Used </h2>

- <b>Windows 10</b> 
- <b>Kali Linux</b> 
<!--
<h2>Program walk-through:</h2>

<p align="center">
Launch the utility: <br/>
<img src="https://i.imgur.com/62TgaWL.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Select the disk:  <br/>
<img src="https://i.imgur.com/tcTyMUE.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Enter the number of passes: <br/>
<img src="https://i.imgur.com/nCIbXbg.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Confirm your selection:  <br/>
<img src="https://i.imgur.com/cdFHBiU.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Wait for process to complete (may take some time):  <br/>
<img src="https://i.imgur.com/JL945Ga.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Sanitization complete:  <br/>
<img src="https://i.imgur.com/K71yaM2.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Observe the wiped disk:  <br/>
<img src="https://i.imgur.com/AeZkvFQ.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
</p>


 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
