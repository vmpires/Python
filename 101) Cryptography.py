from cryptography.fernet import Fernet

key = Fernet.generate_key()

f = Fernet(key)

token = f.encrypt(b"My name is Victor!")

print(token)
print(f.decrypt(token))