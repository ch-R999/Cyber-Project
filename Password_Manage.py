#For storng password locally on the device and using them when needed 
# this will be the first upload 
"""  Method it contain are : 
    1.) To save a Password                         #DONE
    2.) To decrypt and use password when needed
    3.) keping "secret.key" safe in the localhost (Device where code is being implemented)
    4.) ....FUTURE....VIEW
"""
import os
import json
from cryptography.fernet import Fernet

# Generate a key for encryption
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load the key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt the password
def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

# Save password to a JSON file
def save_password(service, password):
    encrypted_password = encrypt_password(password)
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            passwords = json.load(file)
    else:
        passwords = {}
    passwords[service] = encrypted_password.decode()
    with open("passwords.json", "w") as file:
        json.dump(passwords, file)

# Main function to run the password manager
def main():
    generate_key()  # Uncomment this line to generate a new key
    service = input("Enter the service name: ")
    password = input("Enter the password: ")
    save_password(service, password)
    print("Password saved successfully!")

if __name__ == "__main__":
    main()
