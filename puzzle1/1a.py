from puzzle1.functions import calculateFuel

file = "input1.txt"
fuel_sum = 0

with open(file) as f:
    for line in f:
        mass = line.strip()
        fuel = calculateFuel(int(mass))
        fuel_sum += fuel

print("Fuel needed for all modules: " + str(fuel_sum))
