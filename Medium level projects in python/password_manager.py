# Project Name
# Encrypted Password Manager

# Description
# Developed a command-line password manager using Python's cryptography library with Fernet symmetric encryption. The application allows users to securely add and view encrypted passwords. Features include key generation and storage, password encryption and decryption, and user-friendly prompts for managing login credentials.






from cryptography.fernet import Fernet
print("******************************Password Manager******************************")
user = input("What is your name:- ")
def write_key():
  key = Fernet.generate_key()
  with open("key.key", "wb") as key_file:
    key_file.write(key)


def load_key():
    with open("key.key", 'rb') as file:
        key = file.read()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open("password.txt", "r") as file:
      for line in file.readlines():
        data = line.strip()
        name, password = data.split("|")
        print(f"User: {name} and Password: {fer.decrypt(password.encode()).decode()}")
def add():
  name = input(f"{user} Enter your account Name:- ")
  password = input(f"{user} Enter your Password:- ")
  with open("password.txt", "a") as file:
    # file.write(f"Account Name:- {name} and Password {password}")
    file.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")
    print("Login credentials are successfully protected and safely encrypted. ")
while True:
  mode = input("Would you like to add a new password or view a password or press q to quit (add/view/quit):-  ").lower()
  if mode == "q":
    print("Thankyou!")
    quit()
  if mode == 'view':
    view()
  elif mode == 'add':
    add()
  else:
    print("Invalid mode!")
    continue




# Projet Explanation 
# from cryptography.fernet import Fernet 
# The cryptography.fernet module 
# provides a high-level symmetric encryption:
#  mechanism using the Fernet algorithm.
# Here’s a breakdown of what it does:
# Key Concepts
# Symmetric Encryption: Fernet is a symmetric encryption algorithm, meaning it uses the same key for both encryption and decryption.
# This contrasts with asymmetric encryption, which uses a pair of keys (one public and one private).

# Fernet Algorithm:
# The Fernet algorithm is designed to be both secure and easy to use. It guarantees that data encrypted with it cannot be decrypted without the correct key.
# It combines several cryptographic techniques:
# AES (Advanced Encryption Standard) for encryption.
# HMAC (Hash-based Message Authentication Code) for message integrity and authentication.
# HMAC (Hash-based Message Authentication Code) for message integrity and authentication.
# Key Features 
# Key Generation: The module provides functionality to generate a secure key using Fernet.generate_key(). This key must be kept secret as it is required for both encryption and decryption.
#  Encryption/Decryption: The Fernet class allows you to encrypt data with fernet.encrypt(data) and decrypt it with fernet.decrypt(token). The data is securely encrypted and can only be decrypted using the same key.
# Encoding/Decoding: The encrypted data is encoded in a format that is safe to store and transmit, typically base64. The Fernet class handles encoding and decoding automatically.
#  print("******************************Password Manager******************************")
# This line prints the message ***********Password Manager****************
# user = input("What is your name:- ")
# This line takes a name as an input 
'''
def write_key():
  key = Fernet.generate_key()
  with open("key.key", "wb") as key_file:
    key_file.write(key)'''
''' This write_key() function is responsible for generating the key using the 
 line "key = Fernet.generate_key()" in this statement  "Fernet.generate_key()" through this line 
 key is getting generated and storing into "key" variable The next line is "with open("key.key", "wb") as key_file:"
  this line is responsible creating and opening a file name "key.key" and opening it in "wb" mode 
   "wb" mode stands for write bytes and the next line is "key_file.write(key)" and this line is responsible
    for writing that key into the file "key.key" which is responsoble for decrypting the text in passwords.txt'''

'''
def load_key():
    with open("key.key", 'rb') as file:
        key = file.read()
    return key

Open the Key File: The function opens the file key.key in binary read mode ('rb'). 
This mode is necessary because the key is binary data, not text.

Read the Key: file.read() reads the entire content of the file into the variable key. 
Since the key is stored in binary format, it's important to use binary mode when reading it.

Return the Key: The function returns the binary key read from the file. 
'''

'''
"key = load_key()" 

Load the Key: key = 
load_key() calls the load_key function to get the binary key from the key.key file. Then the key is stored in the variable "key"
'''


'''
"fer = Fernet(key)"
Create Fernet Object: 
fer = Fernet(key) creates an instance of the Fernet class using the loaded key. 
This Fernet object (fer) is then used to perform encryption and decryption operations.


what is Fernet?
Fernet is a symmetric encryption algorithm provided by the cryptography library. 
It is designed to be secure and easy to use, offering a straightforward way to encrypt and decrypt data. 
Here's a breakdown of Fernet and its features:
'''