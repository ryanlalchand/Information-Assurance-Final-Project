# Write a separate file that will use the key to encrypt a file and save the encrypted version. Make sure you can also decrypt the file as well.

# import cryptography library and key
from cryptography.fernet import Fernet

file = open("./Part_1/key.key", "rb")
key = file.read()
file.close()

# create file, using key to encypt message and write to file
encrypt_file = open("./Part_1/encrypted_message.txt", "wb")

cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(b"Hello World")
plain_text = cipher_suite.decrypt(cipher_text)

encrypt_file.write(cipher_text)
encrypt_file.close()

# read file and decrypt message
file = open("./Part_1/encrypted_message.txt", "rb")
decrypted_message = cipher_suite.decrypt(file.read())
file.close()

print(cipher_text)
print(decrypted_message)

# write decrypted message to file
file = open("./Part_1/message.txt", "wb")
file.write(decrypted_message)
file.close()