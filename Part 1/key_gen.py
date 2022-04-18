from cryptography.fernet import Fernet

key = Fernet.generate_key()

file = open("key.txt", "w")
file.write(key)
file.close