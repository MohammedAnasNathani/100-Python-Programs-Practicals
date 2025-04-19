with open("example.txt", "w") as file:
    while True:
        user_input = input("Enter text to write (enter '@' to stop): ")
        if user_input == "@":
            break
        file.write(user_input + "\n")

with open("example.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)
