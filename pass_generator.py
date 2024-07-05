import random
import string

def generate_password(length):
    # Define the character sets to generate the password from
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all character sets
    all_characters = lowercase + uppercase + digits + symbols

    # Generate a password using random choices
    password = ''.join(random.choices(all_characters, k=length))
    
    return password

def main():
    # Prompt the user to specify the desired length of the password
    length = int(input("Enter the desired length of the password: "))

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
