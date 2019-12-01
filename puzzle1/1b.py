from functions import *

file = "input1.txt"

fuel_sum = 0
with open(file) as f:
    for line in f:
        mass = line.strip()
        fuel = deepCalcFuel(int(mass))
        fuel_sum += fuel

print("Fuel needed for all modules (with deep calculation): " + str(fuel_sum))