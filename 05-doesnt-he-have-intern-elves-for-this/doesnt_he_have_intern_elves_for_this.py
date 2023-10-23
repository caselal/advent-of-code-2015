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
def find_indexes(string, substring):
    start = 0
    indexes = []

    while start < len(string):
        start = string.find(substring, start)

        if start == -1:
            return indexes

        indexes.append(start)

        start += len(substring)

    return indexes


strings_nice = 0

for s in strings_list:
    count_two_letters = 0
    count_one_letter_between = 0

    # Identify strings containing pairs of any two letters that appear at least twice in the string without overlapping
    all_substrings_count = {}

    all_substrings = [s[i:i + 2] for i in range(len(s) - 1)]
    all_substrings_unique = set(all_substrings)
    all_substrings_unique = list(all_substrings_unique)

    for substring in all_substrings_unique:
        if len(find_indexes(s, substring)) > 1:
            all_substrings_count[substring] = 1

    count_two_letters = len(all_substrings_count)

    # Identify strings containing at least one letter which repeats with exactly one letter between them
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            count_one_letter_between += 1

    if (count_two_letters > 0) and (count_one_letter_between > 0):
        strings_nice += 1

print(strings_nice)
