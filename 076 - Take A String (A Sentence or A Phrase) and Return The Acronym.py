def generate_acronym():
    sentence = input("Enter a sentence or phrase: ")
    words = sentence.split()
    acronym = "".join(word[0].upper() for word in words)
    print(f"Acronym: {acronym}")

generate_acronym()
