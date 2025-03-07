import itertools
import os
import string
import numpy as np
from collections import Counter

# (Caesar Cipher)
def caesar_encrypt(text, shift, encrypt=True):
    if shift > 26:
        return "Error!"

    if not encrypt:
        shift = -shift

    result = ""
    for char in text:
        if 'A' <= char <= 'Z':  
            new_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            result += new_char
        elif 'a' <= char <= 'z': 
            new_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            result += new_char
        elif char.isdigit():
            new_char = chr(((ord(char) - ord('0') + shift) % 10) + ord('0'))
            result += new_char
        elif char == " ":
            result += " "  
        elif 32 <= ord(char) <= 126: 
            new_char = chr(((ord(char) - 32 + shift) % 95) + 32)
            result += new_char
        else:
            result += char
    return result

def caesar_decrypt_brute_force(ciphertext):
    print("\nBrute Force Attempts:")
    for shift in range(1, 26): 
        decrypted_text = caesar_encrypt(ciphertext, shift, encrypt=False)
        print(f"Shift {shift}: {decrypted_text}")

# Vigenere Cipher)
def vigenere(text, key, encrypt=True):
    result = ""
    key = key.lower()
    key_length = len(key)
    key_index = 0

    for char in text:
        if char == " ":
            result += " "  
            continue

        shift = ord(key[key_index % key_length]) - ord('a')
        shift = shift if encrypt else -shift
        
        if 'A' <= char <= 'Z':
            new_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            result += new_char
        elif 'a' <= char <= 'z':
            new_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            result += new_char
        elif char.isdigit():
            new_char = chr(((ord(char) - ord('0') + shift) % 10) + ord('0'))
            result += new_char
        elif 32 <= ord(char) <= 126:
            new_char = chr(((ord(char) - 32 + shift) % 95) + 32)
            result += new_char
        else:
            result += char

        key_index += 1  
    
    return result  

# Monoalphabetic Cipher Encryption

def monoalphabetic_encrypt(text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key_map = {alphabet[i]: key[i] for i in range(len(alphabet))}
    result = "".join(key_map.get(char.upper(), char).lower() if char.islower() else key_map.get(char, char) for char in text)
    return result

# Monoalphabetic Cipher Decryption
def monoalphabetic_decrypt(ciphertext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key_map = {key[i]: alphabet[i] for i in range(len(alphabet))}
    result = "".join(key_map.get(char.upper(), char).lower() if char.islower() else key_map.get(char, char) for char in ciphertext)
    return result

# Distributing the most common letters in the English language
ENGLISH_FREQ_ORDER = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
def frequency_analysis_decrypt(ciphertext):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter_counts = Counter([char for char in ciphertext.upper() if char in alphabet])
    sorted_cipher_letters = [pair[0] for pair in letter_counts.most_common()]
    guessed_key = {cipher_letter: ENGLISH_FREQ_ORDER[i] for i, cipher_letter in enumerate(sorted_cipher_letters) if i < len(ENGLISH_FREQ_ORDER)}
    decrypted_text = "".join(guessed_key.get(char.upper(), char).lower() if char.islower() else guessed_key.get(char.upper(), char) for char in ciphertext)
    return decrypted_text


# Playfair Cipher
def create_playfair_matrix(keyword):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    keyword = "".join(dict.fromkeys(keyword.upper().replace("J", "I")))
    matrix_chars = keyword + "".join([c for c in alphabet if c not in keyword])
    return np.array(list(matrix_chars)).reshape(5, 5)

def find_position(matrix, letter):
    letter = 'I' if letter == 'J' else letter
    for i in range(5):
        for j in range(5):
            if matrix[i, j] == letter:
                return i, j
    return None

def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = "".join([c for c in text if c.isalpha()])
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else 'X'
        if a == b:
            pairs.append((a, 'X'))
            i += 1
        else:
            pairs.append((a, b))
            i += 2
    return pairs

def playfair_cipher(text, matrix, mode=1):
    pairs = prepare_text(text)
    result = []
    for a, b in pairs:
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)
        
        if row_a == row_b:
            result.append(matrix[row_a, (col_a + mode) % 5])
            result.append(matrix[row_b, (col_b + mode) % 5])
        elif col_a == col_b:
            result.append(matrix[(row_a + mode) % 5, col_a])
            result.append(matrix[(row_b + mode) % 5, col_b])
        else:
            result.append(matrix[row_a, col_b])
            result.append(matrix[row_b, col_a])
    
    return "".join(result)

def playfair_encrypt(plaintext, keyword):
    matrix = create_playfair_matrix(keyword)
    return playfair_cipher(plaintext, matrix, mode=1)

def playfair_decrypt(ciphertext, keyword):
    matrix = create_playfair_matrix(keyword)
    return playfair_cipher(ciphertext, matrix, mode=-1)
# (Main Menu)
print("Choose the type of algorithm:")    
print(" 1- Caesar ")
print(" 2- Vigenere")
print(" 3- Monoalphabetic")
print(" 4- Frequency Analysis")
print(" 5- Playfair Cipher")

choice = input("Enter your number: ")
text = input("Enter your text: ")

if choice == "1":
    shift = int(input("Enter shift: "))
    operation = input("Encrypt (E) or Decrypt (D)? ").upper()
    result = caesar_encrypt(text, shift, encrypt=(operation == "E"))
    print("Result:", result)

elif choice == "2":
    key = input("Enter the key: ")
    operation = input("Encrypt (E) or Decrypt (D)? ").upper()
    result = vigenere(text, key, encrypt=(operation == "E"))
    print("Result:", result)

elif choice == "3":
    key = input("Enter substitution key (26 letters): ")
    operation = input("Encrypt (E) or Decrypt (D)? ").upper()
    result = monoalphabetic_encrypt(text, key) if operation == "E" else monoalphabetic_decrypt(text, key)
    print("Result:", result)

elif choice == "4":
    result = frequency_analysis_decrypt(text)
    print("Decrypted text (frequency analysis):", result)

elif choice == "5":
    keyword = input("Enter Playfair keyword: ")
    operation = input("Encrypt (E) or Decrypt (D)? ").upper()
    result = playfair_encrypt(text, keyword) if operation == "E" else playfair_decrypt(text, keyword)
    print("Result:", result)

else:
    print("Invalid choice!")
