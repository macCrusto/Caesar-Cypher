# Programming Assignments

This repository contains implementations of various programming assignments for my Software Techniques course.

## Assignments

### 1. Caesar Cipher Implementation

#### Overview
This repository contains a Python implementation of the Caesar cipher encryption technique. The Caesar cipher is one of the simplest and oldest known encryption techniques, named after Julius Caesar who reportedly used it to communicate with his generals.

#### Features
- **Encode messages** using a specified shift value
- **Decode messages** using the original shift value
- User-friendly command-line interface
- Preserves case (uppercase/lowercase) of letters
- Maintains non-alphabetic characters (spaces, punctuation)
- Input validation for shift values

[More details about the Caesar Cipher implementation](./caesar_cipher_readme.md)

### 2. CGPA Calculator

#### Overview
This program calculates a student's Cumulative Grade Point Average (CGPA) based on the grades received in various courses and their respective credit units.

#### Features
- Input validation for course details
- Support for standard letter grades (A, B, C, D, F)
- Detailed summary of course performance
- Calculation of overall CGPA with proper weighting by credit units
- User-friendly command-line interface

## Repository Structure
```
.
├── README.md                  # Main repository README
├── caesar_cipher.py           # Caesar cipher implementation
├── caesar_cipher_readme.md    # Detailed documentation for Caesar cipher
├── cgpa_calculator.py         # CGPA calculator implementation
```

## Requirements
- Python 3.0 and above

## Usage
Each program can be run independently:

```
# To run the Caesar cipher program
python caesar_cipher.py

# To run the CGPA calculator
python cgpa_calculator.py
```

## Course Information
These assignments were completed as part of the Software Techniques course (Course Code: EIE326) at [Covenant University](https://www.covenantuniversity.edu.ng/).
