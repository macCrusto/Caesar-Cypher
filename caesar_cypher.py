"""
Caesar Cypher Implementation
Author: Ayuba Mathias
Course: EIE326 - Software Techniques
Topic: Python Programming
Assignment: Implementation of Caesar Cypher for Encoding and Decoding Messages

This program implements the Caesar cypher encryption technique where each letter
in the plaintext is shifted a certain number of places down or up the alphabet.
The program provides functionality to both encode and decode messages using
a user-specified shift value.
"""

def encrypt(text, shift):
    """
    Encrypt the given text using Caesar cypher with the specified shift.
    
    Args:
        text (str): The plaintext to encrypt
        shift (int): The number of positions to shift each character
        
    Returns:
        str: The encrypted text
    """
    result = ""
    
    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Convert to 0-25 (A-Z), shift, and convert back to ASCII
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        # Check if the character is a lowercase letter
        elif char.islower():
            # Convert to 0-25 (a-z), shift, and convert back to ASCII
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        # Keep non-letter characters unchanged
        else:
            result += char
    
    return result


def decrypt(text, shift):
    """
    Decrypt the given text using Caesar cypher with the specified shift.
    
    Args:
        text (str): The ciphertext to decrypt
        shift (int): The number of positions that were used to encrypt
        
    Returns:
        str: The decrypted text
    """
    # To decrypt, we can use the encrypt function with a negative shift
    return encrypt(text, -shift)


def get_valid_shift():
    """
    Get a valid shift value from the user.
    
    Returns:
        int: A shift value between 1 and 25
    """
    while True:
        try:
            shift = int(input("Enter the shift value (1-25): "))
            if 1 <= shift <= 25:
                return shift
            else:
                print("Shift must be between 1 and 25. Please try again.")
        except ValueError:
            print("Please enter a valid number.")


def encode_message():
    """Function to handle the message encoding process"""
    message = input("Enter the message to encode: ")
    shift = get_valid_shift()
    
    encrypted_message = encrypt(message, shift)
    
    print("\nEncoded message:")
    print(encrypted_message)
    print(f"Shift used: {shift}")
    print()


def decode_message():
    """Function to handle the message decoding process"""
    message = input("Enter the message to decode: ")
    shift = get_valid_shift()
    
    decrypted_message = decrypt(message, shift)
    
    print("\nDecoded message:")
    print(decrypted_message)
    print(f"Shift used: {shift}")
    print()


def main():
    """Main function to run the Caesar cypher program"""
    print("===== Caesar Cypher Program =====")
    print("Welcome to the Caesar Cypher Encoder/Decoder!")
    print("This program allows you to encode and decode messages using the Caesar cypher technique.")
    
    continue_program = True
    
    while continue_program:
        print("\nWhat would you like to do?")
        choice = input("Enter 'E' to encode, 'D' to decode: ").upper()
        
        if choice == "E":
            encode_message()
        elif choice == "D":
            decode_message()
        else:
            print("Invalid choice. Please enter 'E' or 'D'.")
            continue
        
        continue_choice = input("Would you like to continue? (C) or end the program? (E): ").upper()
        if continue_choice != "C":
            continue_program = False
    
    print("\nThank you for using the Caesar Cypher Program!")


if __name__ == "__main__":
    main()
