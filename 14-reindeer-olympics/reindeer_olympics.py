"""
Advent of Code - Day 14: Reindeer Olympics
"""
import math

# load text file
with open("input.txt", "r") as input:
    descriptions = input.read()
    reindeer_descriptions = descriptions.splitlines()


def reindeer_info(info):
    reindeer_desc = info.split(" ")
    reindeer, speed, flying_duration, resting_period = (
        reindeer_desc[0],
        int(reindeer_desc[3]),
        int(reindeer_desc[6]),
        int(reindeer_desc[-2]),
    )
    return reindeer, speed, flying_duration, resting_period


t = 2503

###########
# Part One
###########
distances_traveled = {}

for description in reindeer_descriptions:
    reindeer, speed, flying_duration, resting_period = reindeer_info(description)
    cycle_length = flying_duration + resting_period
    cycles = math.floor(t / cycle_length)
    distance_traveled = speed * (
        (flying_duration * cycles) + min(flying_duration, t % cycle_length)
    )
    distances_traveled[reindeer] = distance_traveled

# print(distances_traveled)
print(max(zip(distances_traveled.values(), distances_traveled.keys())))

###########
# Part Two
###########s
reindeer_scoring = {}

for description in reindeer_descriptions:
    reindeer, speed, flying_duration, resting_period = reindeer_info(description)
    reindeer_scoring[reindeer] = {
        "speed": speed,
        "flying_duration": flying_duration,
        "resting_period": resting_period,
        "distance_traveled": 0,
        "points": 0,
    }

all_reindeer = list(reindeer_scoring.keys())
distance_tracked = {}

for s in range(1, t + 1):
    for reindeer in all_reindeer:
        reindeer_dict = reindeer_scoring.get(reindeer)
        cycle_length = reindeer_dict.get("flying_duration") + reindeer_dict.get(
            "resting_period"
        )
        cycles = math.floor(s / cycle_length)

        if (s - (cycle_length * cycles) > 0) and (
            s - (cycle_length * cycles) <= reindeer_dict.get("flying_duration")
        ):
            reindeer_dict["distance_traveled"] += reindeer_dict.get("speed")

        distance_tracked[reindeer] = reindeer_dict["distance_traveled"]

    max_distance = max(zip(distance_tracked.values(), distance_tracked.keys()))[0]
    lead_reindeer = [
        lead for lead, distance in distance_tracked.items() if distance == max_distance
    ]
    for l in lead_reindeer:
        reindeer_scoring.get(l)["points"] += 1

all_reindeer_points = {}
for reindeer in all_reindeer:
    all_reindeer_points[reindeer] = reindeer_scoring.get(reindeer).get("points")
max_points = max(zip(all_reindeer_points.values(), all_reindeer_points.keys()))[0]

# print(reindeer_scoring)
print(max_points)
