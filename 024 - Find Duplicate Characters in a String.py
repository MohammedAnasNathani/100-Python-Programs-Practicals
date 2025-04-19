def find_duplicates(input_string):
    char_count = {}
    duplicates = set() 

    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1

    for char, count in char_count.items():
        if count > 1:
            duplicates.add(char)

    return list(duplicates) 

string = input("Enter a string: ")
duplicate_list = find_duplicates(string)
if duplicate_list:
    print("Duplicate characters found:", duplicate_list)
else:
    print("No duplicate characters found.")