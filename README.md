# Information Assurance Final Project

CSIS 3755 Encryption Project

Team: Ryan Lalchand & Kelly Lam

## Part 1: Symmetric key encryption using python

- Research the python library cryptography and rsa.
- Download python if you do not have it already and add it to path when downloading. Follow this video for assistance: https://tajones01.people.ysu.edu
- Install the libraries from the command line similar to how I install matplotlib in the video above\*
  - \*I created a dependecy file, so instead run `python3 -m pip install -r requirements.txt` to install all dependencies on Mac/Linux.
- Using the cryptography library, write a code to generate a key and save it to a file
- Write a separate file that will use the key to encrypt a file and save the encrypted version. Make sure you can also decrypt the file as well.
- Submit to me the codes, the encrypted and decrypted file and the key.

## Part 2: Asymmetric key encryption using python

- Import the rsa library
- Use the rsa library to generate a key pair and save them
- Make a copy of the key from part 1 and place it in a file called rsa_sym_key_plain.txt
- Encrypt that file using the rsa key pair you generated. Place the encrypted version into a file called rsa_sym_key_cipher.txt
- Test it and make sure that you can decrypt it back to plain text.

## Part 3: Presentation

- Record a video between 3-5 min (its okay to go over a little bit but not much please) and submit everything to me in a zipped folder called “lastname_firstname_encryption_project” that contains folders with part 1, 2, and 3 respectively.
