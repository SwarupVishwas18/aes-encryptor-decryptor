"""
Used with permission (when credit given):
- Jake Krajewski, 2020.
"""
from cryptography.fernet import Fernet


class FernetCipher():

    def __init__(self):
        try:
            self.key = self.load_key()
            print("Rada")
            if self.key == "":
                print(2)
                raise FileNotFoundError
        except:
            self.generate_key()
            self.key = self.load_key()
            print("Hello")

        self.f = Fernet(self.key)

    def generate_key(self):
        key = Fernet.generate_key()
        with open('secret.key', 'wb') as key_file:
            key_file.write(key)

    def load_key(self):
        return open('secret.key', 'rb').read()

    def encrypt(self, msg):
        msg = msg.encode()  # byte encode
        enc_msg = self.f.encrypt(msg)
        return enc_msg

    def decrypt(self, msg):
        dec_msg = self.f.decrypt(msg)
        return dec_msg

# print(cd)

# bf = fer.decrypt(cd)
# print(bf)