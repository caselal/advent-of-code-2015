"""
Advent of Code - Day 16: Aunt Sue
"""

###########
# Part One
###########
# load data file
with open("input.txt", "r") as input:
    puzzle_input = input.read()
    puzzle_input = puzzle_input.splitlines()

ticker_tape = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

sample_compounds_set = set(ticker_tape.keys())


def parse_information(input_string):
    string = input_string.split(": ", 1)
    aunt_information = {}
    aunt_number = string[0]
    compounds = string[1].split(", ")

    for compound in compounds:
        aunt_information[compound.split(": ")[0]] = int(compound.split(": ")[1])

    return aunt_number, aunt_information


aunt_sue = ""
compound_count = 0
for string in puzzle_input:
    count = 0
    aunt_number, aunt_information = parse_information(string)

    aunt_compounds_set = set(aunt_information.keys())
    common_compounds = sample_compounds_set.intersection(aunt_compounds_set)

    for compound in common_compounds:
        if ticker_tape.get(compound) == aunt_information.get(compound):
            count += 1

    if count > compound_count:
        aunt_sue = aunt_number
        compound_count = count


print(aunt_sue)

###########
# Part Two
###########
