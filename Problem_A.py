import secrets
import string

class PasswordGenerator:
    def __init__(self):
        self.weak_words = ["Turing", "Knuth", "Lovelace", "Dijkstra", "Hopper", "Shannon"]
        self.letters = string.ascii_letters 
        self.digits = string.digits       
        self.punctuation = string.punctuation 

    def generate_weak_password(self):
        return secrets.choice(self.weak_words) + secrets.choice(self.weak_words)

    def generate_strong_password(self, length):
        characters = self.letters + self.digits + self.punctuation
        while True:
            password = ''.join(secrets.choice(characters) for _ in range(length))
            if (any(c.islower() for c in password) and 
                any(c.isupper() for c in password) and 
                any(c.isdigit() for c in password) and 
                any(c in self.punctuation for c in password)):
                return password

    def generate(self, strength='strong', length=12):
        if strength == 'weak':
            return self.generate_weak_password()
        elif strength == 'medium':
            characters = self.letters + self.digits
            return ''.join(secrets.choice(characters) for _ in range(length))
        else:  # strong
            return self.generate_strong_password(length)

def main():
    generator = PasswordGenerator()
    
    strength = input("Enter the desired strength of the password (weak, medium, strong): ").lower()
    if strength not in ['weak', 'medium', 'strong']:
        print("Invalid strength. Defaulting to strong.")
        strength = 'strong'

    length = 6 if strength == 'weak' else 12
    try:
        if strength != 'weak':
            length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Invalid length. Defaulting to 12.")

    password = generator.generate(strength, length)
    print(f"Generated password: {password}")

main()

