from functions import intcode

file = "input1.txt"

with open(file) as f:
    for line in f:

        input_split = line.split(',')

input_split[1] = 12
input_split[2] = 2

print(input_split)

input_split = intcode(input_split)

print("Position 0: " + input_split[0])
