import numpy as np
import math
from collections import defaultdict

filepath = "input/10.txt"
asteroids = []
starmap = []

with open(filepath) as fp:
    line = fp.readline()
    y = 0
    while line:
        starmap.append(line.strip())
        new = [(x, y) for (x, c) in enumerate(line) if c == "#"]
        asteroids.extend(new)
        y += 1
        line = fp.readline()


def count_blockages(rock_i, rock_j, starmap):
    step = [y - x for (x, y) in zip(rock_i, rock_j)]
    gcd = math.gcd(step[0], step[1])
    step = [int(x / gcd) for x in step]
    loc = [x + y for (x, y) in zip(rock_i, step)]
    count = 0
    while tuple(loc) != rock_j:
        if starmap[loc[1]][loc[0]] == "#":
            count += 1
        loc = [x + y for (x, y) in zip(loc, step)]

    return count


detect = {(i, i): False for i in range(len(asteroids))}
for (i, rock_i) in enumerate(asteroids):
    for (j, rock_j) in enumerate(asteroids):
        if j > i:
            count = count_blockages(rock_i, rock_j, starmap)
            sight = count == 0
            detect[(i, j)] = sight
            detect[(j, i)] = sight

best = None
count = -1
for (i, rock) in enumerate(asteroids):
    new = len([j for j in range(len(asteroids)) if detect[(i, j)]])
    if new > count:
        best = rock
        count = new

print("Part One:", count)


def compute_angle(rock_i, rock_j, starmap):
    step = [y - x for (x, y) in zip(rock_i, rock_j)]
    angle = np.arctan2(step[0], -step[1])
    if angle < 0:
        angle += 2 * np.pi
    angle += 2 * np.pi * count_blockages(rock_i, rock_j, starmap)
    return angle


other_rocks = [x for x in asteroids if x != best]
arr = [(compute_angle(best, rock, starmap), rock) for rock in other_rocks]
arr = sorted(arr, key=lambda x: x[0])

print("Part Two:", arr[199][1][0] * 100 + arr[199][1][1])
