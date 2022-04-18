from cryptography.fernet import Fernet

file = open("key.txt", "r")
key = file.read()
file.close()

encrypt_file = open("message.txt", "w")
encrypt_file.write("Hello World")
encrypt_file.close()

cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(encrypt_file.read())
plain_text = cipher_suite.decrypt(cipher_text)

print(cipher_text)
print(plain_text)

encrypted_file = open("encrypted_message.txt", "w")
encrypted_file.write(cipher_text)
encrypted_file.close()
