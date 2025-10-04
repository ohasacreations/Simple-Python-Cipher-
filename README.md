Modular Arithmetic-Based Numerical Cipher (Modulus 8)
This repository contains a Python implementation of a simple, reversible numerical cipher designed for demonstration and educational purposes, specifically to illustrate the application of modular arithmetic.

1. Principles of Operation
The cipher operates on a digit-by-digit basis, transforming each input digit d into an encrypted digit e within the field of modulo 8.

Input Constraints
The cryptographic scheme is derived from an 8-point mapping table, making it optimally reversible and predictable for input digits in the range of 1 to 8. While the script processes all single-digit inputs, the defined logic directly corresponds to this specific range.

1.1 Encryption Function (encript)
The transformation applies a constant shift of +5 and then utilizes the modulo 8 operation to ensure the output remains within the set {0,1,2,3,4,5,6,7}.

The encryption formula is defined as:

Encrypted Digit e=(d+5)mod8
1.2 Decryption Function (decript)
Decryption reverses the shift operation. In modular arithmetic, subtracting 5 is equivalent to adding 3 (since 3−8=−5). The function implements a piecewise solution to correctly map the encrypted digit back to its original value, compensating for the modular wrap.

Encrypted Digit e

Decryption Operation

Decrypted Digit d

6 or 7

e−5

1 or 2

0 through 5

e+3

3 through 8

2. Implementation
Prerequisites
The script requires a standard Python 3 environment.

Usage
Save the code below into a file named pin_crypto.py.

Execute the script from the command line:

python pin_crypto.py

The console will prompt the user for input for both encryption and decryption tests.

3. Source Code (pin_crypto.py)
def encript(Pin: str) -> str:
    """
    Encrypts a numerical PIN using the (digit + 5) % 8 scheme.
    
    Args:
        Pin: The original PIN number as a string.
        
    Returns:
        The encrypted PIN as a string.
    """
    Epin = ""
    for x in Pin:
        try:
            # Ensure the input is treated as an integer digit
            digit = int(x)
            
            # Apply the encryption formula: (d + 5) mod 8
            num = (digit + 5) % 8
            
            Epin = Epin + str(num)
        except ValueError:
            # Ignores non-digit characters for robust input handling
            pass 
    return Epin

def decript(Epin: str) -> str:
    """
    Decrypts an encrypted PIN using the inverse logic.
    
    Args:
        Epin: The encrypted PIN number as a string.
        
    Returns:
        The decrypted (original) PIN as a string.
    """
    Dpin = ""
    for x in Epin:
        try:
            digit = int(x)
            
            # Decryption logic based on the range of the encrypted digit
            if digit == 6 or digit == 7:
                # Corresponds to subtracting 5 for lower original values
                Dpin = Dpin + str(digit - 5)
            else:
                # Corresponds to adding 3 (equivalent to -5 mod 8) for higher original values
                Dpin = Dpin + str(digit + 3)
                
        except ValueError:
            # Ignores non-digit characters for robust input handling
            pass
            
    return Dpin

# --- Main Program Execution ---

if __name__ == "__main__":
    print("--- Modular PIN Cipher Demonstration ---")
    
    # Recommend digits 1-8 to the user to align with the cipher's design
    userPin = input("Enter the Pin Number (Digits 1-8 recommended): ")
    Encripted_Pin = encript(userPin)
    print(f"\n[Encryption] Original Pin:    {userPin}")
    print(f"[Encryption] Encrypted Pin: {Encripted_Pin}")
    print("-" * 40)

    # Decryption Test
    userEpin = input("Enter the Encrypted Pin Numbber: ")
    Decripted_Pin = decript(userEpin)
    print(f"\n[Decryption] Encrypted Pin: {userEpin}")
    print(f"[Decryption] Decrypted Pin: {Decripted_Pin}")
    print("----------------------------------------")
