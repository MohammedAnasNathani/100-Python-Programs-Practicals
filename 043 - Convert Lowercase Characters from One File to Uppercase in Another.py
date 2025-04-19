with open("source.txt", "r") as source_file:
    content = source_file.read()

uppercase_content = content.upper()

with open("uppercase.txt", "w") as target_file:
    target_file.write(uppercase_content)

print("Converted lowercase to uppercase and saved to uppercase.txt.")
