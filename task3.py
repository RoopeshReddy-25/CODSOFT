import string
import random

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    
    if length < 4:
        print(" Password length should be at least 4 for security.")
        return None
    
    password = "".join(random.choice(characters) for _ in range(length))
    return password

def main():
    print(" Welcome to the Password Generator ")
    try:
        length = int(input(" Enter the desired password length: "))
    except ValueError:
        print(" Please enter a valid number.")
        return
    
    password = generate_password(length)
    if password:
        print("\nGenerated Password: ", password)

if __name__ == "__main__":
    main() 