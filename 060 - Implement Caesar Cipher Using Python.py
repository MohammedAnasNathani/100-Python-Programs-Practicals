def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = 65 if char.isupper() else 97
            result += chr((ord(char) + shift - start) % 26 + start)
        else:
            result += char
    return result

text = "Hello, World!"
shift = 3
encrypted = caesar_cipher(text, shift)
print(f"Encrypted text: {encrypted}")
