# 🔐 Cryptography Algorithms Suite 🛡️

A Python command-line interface (CLI) application that implements various classic cryptographic algorithms. It allows users to encrypt, decrypt, and even attempt to crack ciphers using brute force and frequency analysis.

## ✨ Supported Ciphers & Features

* **🛡️ Caesar Cipher:**
    * Encrypt and Decrypt using a known shift.
    * Brute Force attack to crack the ciphertext without knowing the shift key.
* **🔑 Vigenère Cipher:**
    * Encrypt and Decrypt using a custom keyword.
    * Brute force cracking capabilities for short key lengths.
* **🔀 Monoalphabetic Cipher:**
    * Encrypt and Decrypt using a custom 26-letter substitution alphabet.
    * **Frequency Analysis:** Crack the cipher intelligently by analyzing letter frequencies in the English language.
    * Brute Force attack (demonstration purpose).
* **🔠 Playfair Cipher:**
    * Encrypt and Decrypt text using the Playfair 5x5 matrix generation based on a keyword.
    * Automatically handles duplicate letters and text preparation (e.g., swapping 'J' for 'I').

## 🚀 How to Run

1.  Ensure you have Python 3.x and `numpy` installed:
    ```bash
    pip install numpy
    ```
2.  Run the Python script in your terminal:
    ```bash
    python ciphers_tool.py
    ```
3.  Follow the interactive on-screen menu to choose your algorithm, enter your text, and select whether you want to encrypt, decrypt, or crack!

## 🛠️ Project Structure
* **Caesar Cipher:** Shift-based substitution.
* **Vigenere Cipher:** Polyalphabetic substitution using a keyword.
* **Monoalphabetic:** 1-to-1 fixed alphabet substitution.
* **Playfair:** Polygraphic substitution using a 5x5 grid.

## 🤝 Contributing
Feel free to fork this repository and add more classic ciphers like the Enigma machine, RSA basics, or the Hill Cipher!
