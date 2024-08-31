"""
Advent of Code - Day 13: Knights of the Dinner Table
"""

# load text file
with open("input.txt", "r") as input:
    potential_happiness = input.read()
    potential_happiness_list = potential_happiness.splitlines()


# function to parse potential happiness calculation information
def happiness_calculation_string(string):
    person_1 = string.split(" ")[0]
    person_2 = string.split(" ")[-1].rstrip(".")
    gain_or_lose = string.split(" ")[2]
    match gain_or_lose:
        case "gain":
            happiness_units = int(string.split(" ")[3])
        case "lose":
            happiness_units = -int(string.split(" ")[3])

    return person_1, person_2, happiness_units


# function to generate all possible seating arrangements
def generate_all_seating_arrangements(guests):
    if len(guests) <= 1:
        return [list(guests)]

    seating_result = []
    for guest in guests:
        for seating_arrangement in generate_all_seating_arrangements(guests - {guest}):
            seating_result.append([guest] + seating_arrangement)

    return seating_result


# all_seating_arrangements_itertools = list(itertools.permutations(guest_set))


# function to calculate change in happiness for one seating arrangement
def change_in_happiness_calculation(seating, calculations):
    result = 0
    for i in range(len(seating)):
        if i == len(seating) - 1:
            result += calculations.get((seating[i], seating[0])) + calculations.get(
                (seating[0], seating[i])
            )
        else:
            result += calculations.get((seating[i], seating[i + 1])) + calculations.get(
                (seating[i + 1], seating[i])
            )

    return result


###########
# Part One
###########
guest_set = set(guest.split(" ")[0] for guest in potential_happiness_list)
guest_list = list(guest_set)

happiness_calculations = {}

for calc in potential_happiness_list:
    person_1, person_2, happiness_units = happiness_calculation_string(calc)
    happiness_calculations[(person_1, person_2)] = happiness_units

total_change_in_happiness = []

for seating_arrangement in generate_all_seating_arrangements(guest_set):
    total_change_in_happiness.append(
        change_in_happiness_calculation(seating_arrangement, happiness_calculations)
    )

print(
    f"Total change in happiness for optimal seating arrangement: {max(total_change_in_happiness)}"
)

###########
# Part Two
###########
guest_set_revised = guest_set.copy()
guest_set_revised.add("Myself")
guest_list_revised = list(guest_set_revised)

happiness_calculations_revised = happiness_calculations.copy()
for guest in guest_list:
    happiness_calculations_revised[("Myself", guest)] = 0
    happiness_calculations_revised[(guest, "Myself")] = 0

revised_total_change_in_happiness = []

for seating_arrangement in generate_all_seating_arrangements(guest_set_revised):
    revised_total_change_in_happiness.append(
        change_in_happiness_calculation(
            seating_arrangement, happiness_calculations_revised
        )
    )

print(
    f"Revised total change in happiness for optimal seating arrangement: {max(revised_total_change_in_happiness)}"
)
