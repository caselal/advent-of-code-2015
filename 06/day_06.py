"""
Advent of Code - Day 6: Probably a Fire Hazard
"""
import numpy as np

# load text file
with open('input.txt', 'r') as input:
    instructions = input.read()
    instructions_list = instructions.splitlines()

# function to parse instructions
def x_y(string):
    if 'turn on' in string:
        lights_action = 'turn on'
    elif 'turn off' in string:
        lights_action = 'turn off'
    elif 'toggle' in string:
        lights_action = 'toggle'

    trimmed_string = string.lstrip(lights_action)

    p1_x, p1_y = int(trimmed_string.split(' through ')[0].split(',')[0]), int(trimmed_string.split(' through ')[0].split(',')[1])
    p2_x, p2_y = int(trimmed_string.split(' through ')[1].split(',')[0]), int(trimmed_string.split(' through ')[1].split(',')[1])

    return lights_action, p1_x, p1_y, p2_x, p2_y

###########
# Part One
###########
lights_grid = np.zeros((1000, 1000), dtype=int)

for instruction in instructions_list:
    action, x_1, y_1, x_2, y_2 = x_y(instruction)

    match action:
        case 'turn on':
            for row in range(y_1, y_2 + 1):
                for column in range(x_1, x_2 + 1):
                    lights_grid[row][column] = 1

        case 'turn off':
            for row in range(y_1, y_2 + 1):
                for column in range(x_1, x_2 + 1):
                    lights_grid[row][column] = 0

        case 'toggle':
            for row in range(y_1, y_2 + 1):
                for column in range(x_1, x_2 + 1):
                    if lights_grid[row][column] == 0:
                        lights_grid[row][column] = 1
                    else:
                        lights_grid[row][column] = 0

print(np.sum(lights_grid))

###########
# Part Two
###########
lights_grid = np.zeros((1000, 1000), dtype=int)

for instruction in instructions_list:
    action, x_1, y_1, x_2, y_2 = x_y(instruction)

    match action:
        case 'turn on':
            for row in range(y_1, y_2 + 1):
                for column in range(x_1, x_2 + 1):
                    lights_grid[row][column] += 1

        case 'turn off':
            for row in range(y_1, y_2 + 1):
                for column in range(x_1, x_2 + 1):
                    if lights_grid[row][column] > 0:
                        lights_grid[row][column] -= 1

        case 'toggle':
            for row in range(y_1, y_2 + 1):
                for column in range(x_1, x_2 + 1):
                    lights_grid[row][column] += 2

print(np.sum(lights_grid))
