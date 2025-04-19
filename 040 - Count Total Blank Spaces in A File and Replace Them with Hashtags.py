with open("example.txt", "r") as file:
    content = file.read()

blank_spaces = content.count(" ")
print(f"Total blank spaces: {blank_spaces}")

modified_content = content.replace(" ", "#")

with open("example_modified.txt", "w") as file:
    file.write(modified_content)

print("Blank spaces replaced with hashtags and saved to 'example_modified.txt'.")
