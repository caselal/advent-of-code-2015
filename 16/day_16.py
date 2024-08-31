"""
Advent of Code - Day 16: Aunt Sue
"""

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


###########
# Part One
###########

for string in puzzle_input:
    aunt_number, aunt_information = parse_information(string)

    aunt_compounds_set = set(aunt_information.keys())
    common_compounds = sample_compounds_set.intersection(aunt_compounds_set)

    if all(
        ticker_tape.get(compound) == aunt_information.get(compound)
        for compound in common_compounds
    ):
        break

print(aunt_number)


###########
# Part Two
###########
# function that compares compound values from the sample to a specific aunt sue
def compare_compounds(common_compound, sample_dict, aunt_dict):
    compound_value_aunt = aunt_dict.get(common_compound)
    compound_value_sample = sample_dict.get(common_compound)

    match common_compound:
        case "cats" | "trees":
            return compound_value_aunt > compound_value_sample

        case "pomeranians" | "goldfish":
            return compound_value_aunt < compound_value_sample

        case _:
            return compound_value_aunt == compound_value_sample


for string in puzzle_input:
    aunt_number, aunt_information = parse_information(string)

    aunt_compounds_set = set(aunt_information.keys())
    common_compounds = sample_compounds_set.intersection(aunt_compounds_set)

    if all(
        compare_compounds(compound, ticker_tape, aunt_information)
        for compound in common_compounds
    ):
        break

print(aunt_number)
