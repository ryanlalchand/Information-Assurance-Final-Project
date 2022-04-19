# Part 2: Asymmetric key encryption using python
# https://stuvel.eu/python-rsa-doc/usage.html

# Import the rsa library
import rsa

# Use the rsa library to generate a key pair and save them
(pubKey, privKey) = rsa.newkeys(512)

# Make a copy of the key from part 1
keyFile = open("./Part_1/key.key", "rb")
pt1Key = keyFile.read()
keyFile.close()

# Place it in a file called rsa_sym_key_plain.txt
plainFile = open("./Part_2/rsa_sym_key_plain.txt", "wb")
plainFile.write(pt1Key)
plainFile.close()

# Encrypt that file using the rsa key pair you generated.
crypto = rsa.encrypt(pt1Key, pubKey)

# Place the encrypted version into a file called rsa_sym_key_cipher.txt
cipherFile = open("./Part_2/rsa_sym_key_cipher.txt", "wb")
cipherFile.write(crypto)
cipherFile.close()

# Test it and make sure that you can decrypt it back to plain text.
message = rsa.decrypt(crypto, privKey)
print(message)