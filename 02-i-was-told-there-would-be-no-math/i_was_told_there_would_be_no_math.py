"""
Advent of Code - Day 2: I Was Told There Would Be No Math
"""
# load text file
with open('input.txt', 'r') as input:
    dimensions = input.read()
    dimensions_list = dimensions.splitlines()

###########
# Part One
###########
wrapping_paper_needed = 0

for present in dimensions_list:
    present_dimensions = present.split("x")
    d_l, d_w, d_h = int(present_dimensions[0]), int(
        present_dimensions[1]), int(present_dimensions[2])

    lw = d_l * d_w
    wh = d_w * d_h
    hl = d_h * d_l
    present_surface_area = 2 * lw + 2 * wh + 2 * hl
    min_area = min(lw, wh, hl)
    wrapping_paper_needed += (present_surface_area + min_area)

print(wrapping_paper_needed)

###########
# Part Two
###########
ribbon_needed = 0

for present in dimensions_list:
    present_dimensions = present.split("x")

    d_l, d_w, d_h = int(present_dimensions[0]), int(
        present_dimensions[1]), int(present_dimensions[2])
    d_list = [d_l, d_w, d_h]
    d_list.sort()
    d_1, d_2 = d_list[0], d_list[1]

    ribbon_present = d_1 + d_1 + d_2 + d_2
    ribbon_bow = d_l * d_w * d_h
    ribbon_needed += (ribbon_present + ribbon_bow)

print(ribbon_needed)
