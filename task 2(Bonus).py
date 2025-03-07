 
from collections import Counter

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
COMMON_LETTERS = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def decrypt_using_frequency_analysis(encrypted_message):
    encrypted_message = encrypted_message.upper()
    frequency_map = Counter(c for c in encrypted_message if c in ALPHABET)
    sorted_frequencies = [char for char, _ in frequency_map.most_common()]
    
    substitution_map = {sorted_frequencies[i]: COMMON_LETTERS[i] for i in range(min(len(sorted_frequencies), len(COMMON_LETTERS)))}
    decrypted_message = "".join(substitution_map.get(c, c) for c in encrypted_message)
    
    print("Most likely decrypted text:", decrypted_message)

if __name__ == "__main__":
    encrypted_message = input("Enter encrypted message: ")
    decrypt_using_frequency_analysis(encrypted_message)





