word_to_count = "Python"

with open("example.txt", "r") as file:
    content = file.read()
    word_count = content.lower().split().count(word_to_count.lower())

print(f"The word '{word_to_count}' appears {word_count} times.")
