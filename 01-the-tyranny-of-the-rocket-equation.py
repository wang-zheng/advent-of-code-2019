import math
import io


def fuel_required(mass):
    fuel = 0
    add_fuel = math.floor(mass / 3) - 2
    while add_fuel > 0:
        fuel = fuel + add_fuel
        mass = add_fuel
        add_fuel = math.floor(mass / 3) - 2

    return fuel


filepath = "input/01.txt"
with open(filepath) as fp:
    line = fp.readline()
    fuel1 = 0
    fuel2 = 0
    while line:
        mass = int(line)
        fuel1 = fuel1 + math.floor(mass / 3) - 2
        fuel2 = fuel2 + fuel_required(mass)
        line = fp.readline()

print("Part One:", fuel1)
print("Part Two:", fuel2)
