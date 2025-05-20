# Caesar Cipher Implementation

## Overview
This repository contains a Python implementation of the Caesar cipher encryption technique. The Caesar cipher is one of the simplest and oldest known encryption techniques, named after Julius Caesar, who reportedly used it to communicate with his generals.

## Features
- **Encode messages** using a specified shift value
- **Decode messages** using the original shift value
- User-friendly command-line interface
- Preserves case (uppercase/lowercase) of letters
- Maintains non-alphabetic characters (spaces, punctuation)
- Input validation for shift values

## How It Works
The Caesar cipher works by shifting each letter in the plaintext by a fixed number of positions in the alphabet. For example, with a shift of 3:
- 'A' becomes 'D'
- 'B' becomes 'E'
- 'Z' becomes 'C' (wrapping around the alphabet)

## Requirements
- Python 3.0 and above

## Usage
1. Clone the repository:
   ```
   git clone https://github.com/macCrusto/Caesar-Cypher.git
   cd caesar-cipher
   ```

2. Run the program:
   ```
   python caesar_cipher.py
   ```

3. Follow the on-screen prompts:
   - Choose to encode (E) or decode (D) a message
   - Enter the message
   - Specify the shift value (1-25)
   - View the result
   - Choose to continue or end the program

## Example

### Encoding
```
===== Caesar Cipher Program =====
Welcome to the Caesar Cipher Encoder/Decoder!
This program allows you to encode and decode messages using the Caesar cipher technique.

What would you like to do?
Enter 'E' to encode, 'D' to decode: E
Enter the message to encode: Hello World
Enter the shift value (1-25): 3

Encoded message:
Khoor Zruog
Shift used: 3
```

### Decoding
```
What would you like to do?
Enter 'E' to encode, 'D' to decode: D
Enter the message to decode: Khoor Zruog
Enter the shift value (1-25): 3

Decoded message:
Hello World
Shift used: 3
```

## Program Structure
- `encrypt()`: Function to encode a message using the specified shift
- `decrypt()`: Function to decode a message using the specified shift
- `get_valid_shift()`: Helper function to validate user input for shift value
- `encode_message()`: Function to handle the message encoding process
- `decode_message()`: Function to handle the message decoding process
- `main()`: Main program function that controls the program flow

## Security Note
The Caesar cipher is considered a weak encryption method by modern standards, as it can be easily broken using brute force (trying all 25 possible shifts) or frequency analysis. This implementation is for educational purposes only and should not be used for securing sensitive information.

## Educational Value
This implementation demonstrates:
- Basic cryptographic concepts
- Character manipulation in Python
- Input validation techniques
- Modular programming with functions
- Command-line user interface design

## Assignment Information
This project was created for a software techniques assignment to demonstrate understanding of basic Python programming.
