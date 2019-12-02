from functions import intcode

file = "input1.txt"

with open(file) as f:
    for line in f:

        input_split = line.split(',')

input_split[1] = 50
input_split[2] = 64

print(input_split)

input_split = intcode(input_split)

print("Position 0: " + input_split[0])
