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

    index = 0
    while index < string_length:
        match characters[index]:
            case '\"':
                pass
            case '\\':
                if characters[index + 1] == '\"' or characters[index + 1] == '\\':
                    index += 1
                else:
                    index += 3
                total_string_values += 1
            case _:
                total_string_values += 1
        index += 1

number_of_characters = total_string_codes - total_string_values
print(total_string_codes, total_string_values, number_of_characters)


###########
# Part Two
###########
total_encoded_string_values = 0

for characters in characters_list:
    index = 0
    while index < len(characters):
        match characters[index]:
            case '"':
                if index > 0 and characters[index - 1] == '\\':
                    total_encoded_string_values += 1
                else:
                    total_encoded_string_values += 2
            case "\\":
                total_encoded_string_values += 1

        total_encoded_string_values += 1
        index += 1

number_of_characters_encoded = total_encoded_string_values - total_string_codes
print(total_encoded_string_values, total_string_codes, number_of_characters_encoded)
