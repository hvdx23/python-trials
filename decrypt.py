from cryptography.fernet import Fernet

def decrypt(s, key):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(s)
    print(f"The decrypted string is {decrypted_message.decode()}")

s = input("Enter the string to be decrypted: ")
key = input("Enter the key: ")
decrypt(s.encode(), key.encode())

