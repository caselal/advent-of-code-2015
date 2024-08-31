"""
Advent of Code - Day 9: All in a Single Night
"""
import math
import itertools

# load text file
with open('input.txt', 'r') as input:
    locations = input.read()
    pairs_of_locations = locations.splitlines()

###########
# Part One
###########
total_locations = set()
for pair in pairs_of_locations:
    cities = pair.split(' = ')[0].split(' ')
    total_locations.add(cities[0])
    total_locations.add(cities[2])

distances_dict = {}

for pair in pairs_of_locations:
    locations = pair.split(' = ')[0]
    distance = pair.split(' = ')[1]
    distances_dict[ (locations.split(' ')[0], locations.split(' ')[2])] = int(distance)
    distances_dict[(locations.split(' ')[2], locations.split(' ')[0])] = int(distance)

#all_routes_itertools = list(itertools.permutations(total_locations))

def generate_all_routes(locations):
    if len(locations) <= 1:
        return [list(locations)]

    result = []
    for location in locations:
        for route in generate_all_routes(locations - {location}):
            result.append([location] + route)
    return result

all_routes = generate_all_routes(total_locations)
total_distance = []
for route in all_routes:
    distance = 0
    for i in range(len(route)-1):
        distance += distances_dict.get((route[i], route[i+1]))
    total_distance.append(distance)

print(min(total_distance))

###########
# Part Two
###########
print(max(total_distance))
