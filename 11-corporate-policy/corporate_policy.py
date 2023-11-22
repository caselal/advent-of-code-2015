"""
Advent of Code - Day 11: Corporate Policy
"""
import string
# load text file
with open('input.txt', 'r') as input:
    current_password = input.read().replace('\n','')

###########
# Part One
###########
letters = string.ascii_lowercase

# function to increment password character
def increment_character(character):
    letter_index = letters.index(character)
    if letter_index == 25:
        next_letter = letters[0]
    else:
        next_letter = letters[letter_index + 1]

    return next_letter

# function to increment next password
def increment_password(old_password):
    new_password = old_password
    for i in range(len(old_password) - 1, -1, -1):
        new_password = new_password[:i] + increment_character(new_password[i]) + new_password[i+1:]

        if new_password[i] != 'a':
            return new_password

    return 'a' + new_password

# function to increment next password with recursion
def increment_password_recursion(old_password):
    if old_password == '':
        return 'a'
    rest = old_password[:-1]
    updated_character = increment_character(old_password[-1])
    if updated_character != 'a':
        return rest + updated_character
    return increment_password_recursion(rest) + updated_character

# function to check if password contains one increasing straight of at least three letters
def password_requirements_1(password):
    count_increasing_letters = 0
    for i in range(len(password) - 3):
        if ord(password[i+2]) - ord(password[i+1]) == 1 and ord(password[i+1]) - ord(password[i]) == 1:
            count_increasing_letters += 1

    return count_increasing_letters > 0

# function to check if password contains the letters i, o, or l
def password_requirements_2(password):
    excluded_letters = set('iol')
    password = set(password)

    return len(password & excluded_letters) == 0

# function to check if password contains at least two different, non-overlapping pairs of letters
def password_requirements_3(password):
    all_substring_pairs = {}

    for i in range(len((password)) - 1):
        if password[i] == password[i + 1]:
            substring = password[i] + password[i + 1]

            if all_substring_pairs.get(substring) is None:
                all_substring_pairs[substring] = i

    return len(all_substring_pairs) > 1

# function to check if password meets all requirements
def all_password_requirements(password):
    return password_requirements_1(password) and password_requirements_2(password) and password_requirements_3(password)

# generate next password meeting all password requirements
next_password = increment_password(current_password)
password_requirements_met = all_password_requirements(next_password)

while password_requirements_met is False:
    next_password = increment_password(next_password)
    password_requirements_met = all_password_requirements(next_password)

print(next_password)

###########
# Part Two
###########
current_password = next_password
next_password = increment_password(current_password)
password_requirements_met = all_password_requirements(next_password)

while password_requirements_met is False:
    next_password = increment_password(next_password)
    password_requirements_met = all_password_requirements(next_password)

print(next_password)
