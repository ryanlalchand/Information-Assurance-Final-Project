# Research the python library cryptography and rsa.
# Download python if you do not have it already and add it to path when downloading. Follow this video for assistance: https://tajones01.people.ysu.edu
# Install the libraries from the command line similar to how I install matplotlib in the video above.
# Run `python3 -m pip install -r requirements.txt` to install all dependencies on Mac/Linux.

# Using the cryptography library, write a code to generate a key and save it to a file

# import cryptography library and generate key
from cryptography.fernet import Fernet
key = Fernet.generate_key()

# write key to file in bytes (not a string)
file = open("./Part_1/key.key", "wb")
file.write(key)
file.close