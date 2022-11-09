import secrets
import string

class Password:
    def __init__(self, length):
        self.salt = self.generate_salt(length//2)
        self.pw = self.generate_password(length) + self.salt
        # TODO: Hash / encrypt pw
        #       Store salt and hashed pw

    def generate_password(length, num_upper=0, num_lower=0):
        alphabet = string.ascii_letters + string.digits
        while True:
            password = ''.join(secrets.choice(alphabet) for i in range(10))
            if (any(c.islower() for c in password)
                    and sum(c.isupper() for c in password) >= num_upper
                    and sum(c.isdigit() for c in password) >= num_lower):
                return password