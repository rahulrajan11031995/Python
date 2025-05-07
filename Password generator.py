import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("🔐 Welcome to the Password Generator!")

while True:
    # Ask for password length
    try:
        length = int(input("\nEnter the desired password length (or 0 to quit): "))
        if length == 0:
            print("Goodbye!")
            break
        elif length < 0:
            print("Please enter a positive number.")
            continue
    except ValueError:
        print("Please enter a valid number.")
        continue

    # Generate and display the password
    password = generate_password(length)
    print("✅ Your generated password is:", password)
