import random
import string

def generate_password(length):
    if length < 4:
        print("For complexity length should be atleast 4 char")
        return None

    # character sets for complexity is lower,upper,digits,symbols
    lwr = string.ascii_lowercase
    upr = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Password has at least one char from each set
    password = [
        random.choice(lwr),
        random.choice(upr),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill rest of password length with random choices 
    if length > 4:
        all_chars = lwr + upr + digits + symbols
        password += random.choices(all_chars, k=length - 4)

    # For randomness we have to shuffle password length
    random.shuffle(password)

    # Convert the list to a string
    return "".join(password)

def main():
    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)
        if password:
            print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
