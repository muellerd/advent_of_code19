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