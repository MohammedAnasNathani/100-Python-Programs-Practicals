with open("source.txt", "r") as source_file:
    content = source_file.read()

lowercase_content = content.lower()

with open("lowercase.txt", "w") as target_file:
    target_file.write(lowercase_content)

print("Converted uppercase to lowercase and saved to lowercase.txt.")
