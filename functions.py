import math

# puzzle 1
def calculateFuel(mass):
    return math.floor(int(mass) / 3) - 2

def deepCalcFuel(mass):
    fuel = calculateFuel(mass)
    if fuel <= 0:
        return 0
    else:
        return fuel + deepCalcFuel(fuel)

# puzzle 2
def intcode(input_split):
    instruction_pointer = 0
    while int(input_split[instruction_pointer]) != 99:
        opCode = int(input_split[instruction_pointer])
        firstPos = int(input_split[instruction_pointer + 1])
        secondPos = int(input_split[instruction_pointer + 2])
        goalPos = int(input_split[instruction_pointer + 3])

        num1 = int(input_split[firstPos])
        num2 = int(input_split[secondPos])

        if opCode == 1:
            input_split[goalPos] = str(num1 + num2)

        if opCode == 2:
            input_split[goalPos] = str(num1 * num2)

        if opCode != 1 and opCode != 2 and opCode != 99:
            print("Unknown opcode. Something went wrong.")

        instruction_pointer += 4
    return input_split