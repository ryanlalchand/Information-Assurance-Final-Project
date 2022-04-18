from cryptography.fernet import Fernet

key = Fernet.generate_key()

file = open("./Part_1/key.key", "wb")
file.write(key)
file.close