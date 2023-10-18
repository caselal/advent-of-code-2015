"""
Advent of Code - Day 1: Not Quite Lisp
"""
# load text file
with open('input.txt', 'r') as input:
    instructions = input.read()

floor = 0
floors = []

for direction in instructions:
    if direction == '(':
        floor += 1
    if direction == ')':
        floor -= 1
    floors.append(floor)

###########
# Part One
###########
print(floor)

###########
# Part Two
###########
print(floors.index(-1) + 1)
