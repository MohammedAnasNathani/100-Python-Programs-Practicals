def caesar_cipher_dict(text, shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    cipher_dict = dict(zip(alphabet, shifted_alphabet))
    
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += cipher_dict[char]
            else:
                result += cipher_dict[char.upper()].lower()
        else:
            result += char
    return result

text = "Hello, World!"
shift = 3
encrypted = caesar_cipher_dict(text, shift)
print(f"Encrypted text: {encrypted}")
