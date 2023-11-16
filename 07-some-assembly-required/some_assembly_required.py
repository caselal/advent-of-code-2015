"""
Advent of Code - Day 7: Some Assembly Required
"""
# load text file
with open('input.txt', 'r') as input:
    booklet = input.read()
    instructions = booklet.splitlines()

###########
# Part One
###########
wire_signals = {}

def bitwise_operation(operation, x, y):
    match operation:
        case 'AND':
            result = x & y
        case 'OR':
            result = x | y
        case 'RSHIFT':
            result = x >> y
        case 'LSHIFT':
            result = x << y

    return result

def signal(wire_signals_dict, string_signal):
    if string_signal.isnumeric():
        output = int(string_signal)
    elif isinstance(wire_signals_dict.get(string_signal), int):
        output = wire_signals_dict.get(string_signal)
    else:
        output = string_signal

    return output

def bitwise_function_not(wire_signals_dict, full_string):
    string = full_string.split(' ')[1]

    if string.isnumeric():
        output = (2**16 - 1) - int(string)
    elif isinstance(wire_signals_dict.get(string), int):
        output = (2**16 - 1) - wire_signals_dict.get(string)
    else:
        output = full_string

    return output

def bitwise_function(wire_signals_dict, string):
    string_1, operation, string_2 = string.split(' ')[0], string.split(' ')[1], string.split(' ')[2]

    if isinstance(wire_signals_dict.get(string_1), int):
        if isinstance(wire_signals_dict.get(string_2), int):
            output = bitwise_operation(operation, wire_signals_dict.get(string_1), wire_signals_dict.get(string_2))
        elif string_2.isnumeric():
            output = bitwise_operation(operation, wire_signals_dict.get(string_1), int(string_2))
        else:
            output = string

    elif string_1.isnumeric():
        if isinstance(wire_signals_dict.get(string_2), int):
            output = bitwise_operation(operation, int(string_1), wire_signals_dict.get(string_2))
        elif string_2.isnumeric():
            output = bitwise_operation(operation, int(string_1), int(string_2))
        else:
            output = string

    else:
        output = string

    return output

for instruction_string in instructions:
    instruction = instruction_string.split(' -> ')
    wire = instruction[1]

    if instruction[0].isnumeric():
        wire_signals[wire] = int(instruction[0])
    else:
        wire_signals[wire] = instruction[0]

wire_signal_values = False
while wire_signal_values is False:
    for key, value in wire_signals.items():
        if not isinstance(value, int):
            if len(value.split(' ')) > 1:
                instruction_length = len(value.split(' '))
            else:
                instruction_length = 1
                wire_signals[key] = signal(wire_signals, value)

            match instruction_length:
                case 2:
                    wire_signals[key] = bitwise_function_not(wire_signals, value)
                case 3:
                    wire_signals[key] = bitwise_function(wire_signals, value)
    wire_signal_values = all(isinstance(signal, int) for signal in list(wire_signals.values()))

print(wire_signals.get('a'))


###########
# Part Two
###########
wire_signals_new = {}

for instruction_string in instructions:
    instruction = instruction_string.split(' -> ')
    wire = instruction[1]

    if instruction[0].isnumeric():
        wire_signals_new[wire] = int(instruction[0])
    else:
        wire_signals_new[wire] = instruction[0]

wire_signals_new['b'] = wire_signals.get('a')

wire_signal_values_new = False
while wire_signal_values_new is False:
    for key, value in wire_signals_new.items():
        if not isinstance(value, int):
            if len(value.split(' ')) > 1:
                instruction_length = len(value.split(' '))
            else:
                instruction_length = 1
                wire_signals_new[key] = signal(wire_signals_new, value)

            match instruction_length:
                case 2:
                    wire_signals_new[key] = bitwise_function_not(wire_signals_new, value)
                case 3:
                    wire_signals_new[key] = bitwise_function(wire_signals_new, value)
    wire_signal_values_new = all(isinstance(signal, int) for signal in list(wire_signals_new.values()))

print(wire_signals_new.get('a'))
