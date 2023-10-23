"""
Advent of Code - Day 5: Doesn't He Have Intern-Elves For This?
"""

# load text file
with open('input.txt', 'r') as input:
    strings = input.read()
    strings_list = strings.splitlines()

###########
# Part One
###########
vowels = {'a', 'e', 'i', 'o', 'u'}
disallowed_substrings = {'ab', 'cd', 'pq', 'xy'}
strings_nice = 0

for s in strings_list:
    count_vowels = 0
    count_double_letters = 0
    count_disallowed_substrings = 0

    for character in s:
        if character in vowels:
            count_vowels += 1

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count_double_letters += 1

        if s[i:i + 2] in disallowed_substrings:
            count_disallowed_substrings += 1

    if (count_vowels > 2) and (count_double_letters >
                               0) and (count_disallowed_substrings < 1):
        strings_nice += 1

print(strings_nice)

###########
# Part Two
###########
strings_nice = 0

for s in strings_list:
    count_two_letters = 0
    count_one_letter_between = 0

    # Identify strings containing pairs of any two letters that appear at least twice in the string without overlapping
    all_substrings = {}

    for i in range(len(s) - 1):
        substring = s[i] + s[i + 1]
        if all_substrings.get(substring) is None:
            all_substrings[substring] = i
        else:
            if all_substrings.get(substring) != i - 1:
                count_two_letters += 1

    # Identify strings containing at least one letter which repeats with exactly one letter between them
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            count_one_letter_between += 1

    if (count_two_letters > 0) and (count_one_letter_between > 0):
        strings_nice += 1

print(strings_nice)
