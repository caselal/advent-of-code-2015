"""
Advent of Code - Day 10: Elves Look, Elves Say
"""
# load text file
with open('input.txt', 'r') as input:
    puzzle_input = input.read().replace('\n','')

# function to read aloud sequence
def read_sequence_aloud(sequence_input):
    sequence_string = ""
    digit_value = sequence_input[0]
    digit_count = 0

    for digit in sequence_input:
        if digit == digit_value:
            digit_count += 1
        else:
            sequence_string += str(digit_count) + digit_value
            digit_value = digit
            digit_count = 1

    sequence_string += str(digit_count) + digit_value

    return sequence_string

# function to apply look and see process n times
def generate_sequences(sequence_input, n_times):

    previous_sequence = sequence_input

    for i in range(n_times):
        next_sequence = read_sequence_aloud(previous_sequence)
        previous_sequence = next_sequence

    return next_sequence

###########
# Part One
###########
print(len(generate_sequences(puzzle_input, 40)))


###########
# Part Two
###########
print(len(generate_sequences(puzzle_input, 50)))
