# code for encrytping a string
import cryptography as cryptography
from cryptography.fernet import Fernet


def encrypt(s):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encMessage = fernet.encrypt(s.encode())
    # return encMessage
    print(f"The encrypted string is {encMessage}")
    print(f"The key is {key}")


s = input("Enter the string to be encrypted: ")
encrypt(s)
