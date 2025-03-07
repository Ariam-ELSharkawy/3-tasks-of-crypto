from itertools import permutations

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char in ALPHABET:
            decrypted_text += key[ALPHABET.index(char)]
        else:
            decrypted_text += char
    return decrypted_text

def brute_force_monoalphabetic(cipher_text):
    possible_keys = ["ETAOINSHRDLCUMWFGYPBVKJXQZ", "ZYXWVUTSRQPONMLKJIHGFEDCBA"]  
    for key in possible_keys:
        decrypted_text = decrypt(cipher_text, key)
        print(f"Trying key: {key}\nDecrypted text: {decrypted_text}\n")


cipher_text = input("Enter the encrpted text: ").upper()  
brute_force_monoalphabetic(cipher_text)  


