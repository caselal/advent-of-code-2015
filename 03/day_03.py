"""
Advent of Code - Day 3: Perfectly Spherical Houses in a Vacuum
"""
# load text file
with open('input.txt', 'r') as input:
    directions = input.read()

###########
# Part One
###########
houses_dict = {}
x, y = 0, 0
location = (x, y)
houses_dict[location] = 1

for direction in directions:
    match direction:
        case '^':
            x += 1
        case 'v':
            x -= 1
        case '<':
            y -= 1
        case '>':
            y += 1

    new_location = (x, y)
    houses_dict[new_location] = 1

number_of_houses = len(houses_dict)
print(number_of_houses)

###########
# Part Two
###########
houses_dict = {}

def moves(start, houses_dict):
    x, y = 0, 0
    starting_location = (x, y)
    houses_dict[starting_location] = 1

    for i in range(start, len(directions) - 1, 2):
        match directions[i]:
            case '^':
                x += 1
            case 'v':
                x -= 1
            case '<':
                y -= 1
            case '>':
                y += 1

        new_location = (x, y)
        houses_dict[new_location] = 1

moves(0, houses_dict)
moves(1, houses_dict)

number_of_houses = len(houses_dict)
print(number_of_houses)
