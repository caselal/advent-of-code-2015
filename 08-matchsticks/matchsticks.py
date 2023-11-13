"""
Advent of Code - Day 8: Matchsticks
"""
# load text file
with open('input.txt', 'r') as input:
    characters_input = input.read()
    characters_list = characters_input.splitlines()

###########
# Part One
###########
total_string_codes = 0
total_string_values = 0

for characters in characters_list:
    string_length = len(characters)
    total_string_codes += string_length

    if characters.isalpha():
        total_string_values += string_length - 2
    else:
        index = 1
        while index <= string_length - 2:
            if (characters[index] == "\\" and characters[index + 1] == "\\") or (characters[index] == "\\" and characters[index + 1] == '\"'):
                index += 2
            elif characters[index] == "\\" and characters[index + 1] == "x":
                index += 4
            else:
                index += 1
            total_string_values += 1

number_of_characters = total_string_codes - total_string_values
print(total_string_codes, total_string_values, number_of_characters)


###########
# Part Two
###########
total_encoded_string_values = 0

for characters in characters_list:
    total_encoded_string_values += (len(characters) + 4)

    if not characters.isalpha():
        index = 1
        while index <= len(characters) - 2:
            if (characters[index] == "\\" and characters[index + 1] == "\\") or (characters[index] == "\\" and characters[index + 1] == '\"'):
                index += 2
                total_encoded_string_values += 2
            elif characters[index] == "\\" and characters[index + 1] == "x":
                index += 4
                total_encoded_string_values += 1
            else:
                index += 1
number_of_characters_encoded = total_encoded_string_values - total_string_codes
print(total_encoded_string_values, total_string_codes, number_of_characters_encoded)
