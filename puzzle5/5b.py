from intcode import intcode

file = "input1.txt"

with open(file) as f:
    for line in f:
        input_split = line.split(',')

result = intcode(input_split, 5)