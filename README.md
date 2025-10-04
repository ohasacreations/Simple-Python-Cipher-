# Modular Arithmetic-Based Numerical Cipher (Modulus 8)

This repository presents a Python implementation of a simple, reversible numerical cipher. Its primary purpose is to serve as a clean, runnable demonstration of the application of **modular arithmetic** in cryptographic principles.

***

## 1. Theoretical Framework

The cipher operates by transforming each digit of an input PIN independently, using a modulus of $8$.

### Input Constraint

The cipher is designed and validated based on the $8$-point mapping derived from the original design illustration (which used digits $1$ through $8$). As such, the scheme is optimally reversible and predictable for input digits in the range of $\mathbf{1}$ to $\mathbf{8}$.

### 1.1 Encryption Function $(\text{encript})$

Each input digit $d$ is transformed into an encrypted digit $e$ by applying a shift of $+5$ and then the modulo $8$ operation.

$$\text{Encrypted Digit } e = (d + 5) \bmod 8$$

### 1.2 Decryption Function $(\text{decript})$

Decryption reverses the operation. Since $$-5 \equiv 3 \pmod 8$$ the inverse operation is implemented piecewise to correctly map the encrypted digit $e$ back to the original digit $d$ by compensating for the modular wrap.

| Encrypted Digit $e$ | Decryption Operation | Decrypted Digit $d$ |
| :-----------------: | :------------------: | :-----------------: |
| $6$ or $7$          | $e - 5$              | $1$ or $2$          |
| $0$ through $5$     | $e + 3$              | $3$ through $8$     |

***

## 2. Usage and Execution

### Prerequisites

This script requires a standard **Python 3** environment.

### Running the Cipher

1.  Save the code below into a file named `pin_crypto.py`.
2.  Execute the script from your terminal:

    ```bash
    python pin_crypto.py
    ```

The program will prompt you for a PIN to encrypt and an encrypted PIN to decrypt.

***

## 3. Source Code (`pin_crypto.py`)

```python
def encript(Pin: str) -> str:
    """
    Encrypts a numerical PIN using the (digit + 5) % 8 scheme.
    """
    Epin = ""
    for x in Pin:
        try:
            digit = int(x)
            # Apply the encryption formula: (d + 5) mod 8
            num = (digit + 5) % 8
            Epin = Epin + str(num)
        except ValueError:
            # Simple handling: ignores non-digit characters
            pass 
    return Epin

def decript(Epin: str) -> str:
    """
    Decrypts an encrypted PIN using the inverse logic.
    """
    Dpin = ""
    for x in Epin:
        try:
            digit = int(x)
            
            # Inverse operation: -5 is equivalent to +3 mod 8
            if digit == 6 or digit == 7:
                # Corresponds to subtracting 5 for lower original values
                Dpin = Dpin + str(digit - 5)
            else:
                # Corresponds to adding 3 for higher original values
                Dpin = Dpin + str(digit + 3)
                
        except ValueError:
            # Simple handling: ignores non-digit characters
            pass
            
    return Dpin

# --- Main Program Execution ---

if __name__ == "__main__":
    print("--- Modular PIN Cipher Demonstration ---")
    
    userPin = input("Enter the Pin Number (Digits 1-8 recommended): ")
    Encripted_Pin = encript(userPin)
    print(f"\n[Encryption] Original Pin:    {userPin}")
    print(f"[Encryption] Encrypted Pin: {Encripted_Pin}")
    print("-" * 40)

    userEpin = input("Enter the Encrypted Pin Numbber: ")
    Decripted_Pin = decript(userEpin)
    print(f"\n[Decryption] Encrypted Pin: {userEpin}")
    print(f"[Decryption] Decrypted Pin: {Decripted_Pin}")
    print("----------------------------------------")
