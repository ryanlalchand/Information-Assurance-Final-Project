from cryptography.fernet import Fernet

file = open("./Part_1/key.key", "rb")
key = file.read()
file.close()

encrypt_file = open("./Part_1/encrypted_message.txt", "wb")

cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(b"Hello World")
plain_text = cipher_suite.decrypt(cipher_text)

encrypt_file.write(cipher_text)
encrypt_file.close()

file = open("./Part_1/encrypted_message.txt", "rb")
decrypted_message = cipher_suite.decrypt(file.read())
file.close()

print(cipher_text)
print(decrypted_message)

file = open("./Part_1/message.txt", "wb")
file.write(decrypted_message)
file.close()