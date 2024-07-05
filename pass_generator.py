import random
import string

def generate_password(password_length):
    # Define the character sets to generate the password from
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + symbols

    # Generate a password using random choices
    password = ''.join(random.choices(all_characters, k=password_length))
    
    return password

def main():
    while True:
        # Prompt the user to specify the desired length of the password
        length_input = input("Enter the desired length of the password (numbers only): ")

        # Check if the input consists only of digits
        if length_input.isdigit():
            desired_length = int(length_input)
            break
        else:
            print("Please enter numbers only for password length.")

    # Generate the password
    generated_password = generate_password(desired_length)

    # Display the generated password
    print("Generated Password:", generated_password)

if __name__ == "__main__":
    main()
