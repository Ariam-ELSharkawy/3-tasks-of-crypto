import re

class PlayfairCipher:
    def __init__(self, key):
        
        self.key = re.sub(r'[^A-Z]', '', key.upper().replace("J", "I"))  
        self.matrix = self.generate_matrix()

    def generate_matrix(self):
        
        key_set = "".join(dict.fromkeys(self.key + "ABCDEFGHIKLMNOPQRSTUVWXYZ"))  
        key_set = key_set[:25]  
        return [list(key_set[i:i+5]) for i in range(0, 25, 5)]

    def display_matrix(self):
        
        print("\n5x5 Playfair Matrix:")
        for row in self.matrix:
            print(" ".join(row))

    def prepare_text(self, text):
        
        text = re.sub(r'[^A-Z]', '', text.upper().replace("J", "I"))  
        prepared = ""
        i = 0
        while i < len(text):
            a = text[i]
            if i + 1 < len(text) and text[i] != text[i + 1]:
                b = text[i + 1]
                i += 2
            else:
                b = 'X'  
                i += 1
            prepared += a + b
        return prepared

    def find_position(self, char):
        
        for i, row in enumerate(self.matrix):
            if char in row:
                return i, row.index(char)
        return None

    def process_text(self, text, encrypt=True):
        
        text = self.prepare_text(text)
        result = ""
        shift = 1 if encrypt else -1  

        for i in range(0, len(text), 2):
            r1, c1 = self.find_position(text[i])
            r2, c2 = self.find_position(text[i+1])

            if r1 == r2:  
                result += self.matrix[r1][(c1 + shift) % 5] + self.matrix[r2][(c2 + shift) % 5]
            elif c1 == c2:  
                result += self.matrix[(r1 + shift) % 5][c1] + self.matrix[(r2 + shift) % 5][c2]
            else:  
                result += self.matrix[r1][c2] + self.matrix[r2][c1]

        return result

    def encrypt(self, plaintext):
        
        return self.process_text(plaintext, True)

    def decrypt(self, ciphertext):
        
        return self.process_text(ciphertext, False)

if __name__ == "__main__":
    key = input("Enter keyword: ")
    cipher = PlayfairCipher(key)
    cipher.display_matrix()

    plaintext = input("\nEnter text to encrypt: ")
    encrypted = cipher.encrypt(plaintext)
    print("Encrypted:", encrypted)

    ciphertext = input("\nEnter text to decrypt: ")
    decrypted = cipher.decrypt(ciphertext)
    print("Decrypted:", decrypted)