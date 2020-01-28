import numpy as np

filepath = "input/03.txt"
with open(filepath) as fp:
    line = fp.readline()
    wire1 = line.split(",")
    line = fp.readline()
    wire2 = line.split(",")


def parse(wire):
    position = [0, 0]
    path = [tuple(position)]

    for move in wire:
        direction = move[0]
        distance = int(move[1:])

        if direction == "L":
            position[0] -= distance
        elif direction == "R":
            position[0] += distance
        elif direction == "U":
            position[1] += distance
        elif direction == "D":
            position[1] -= distance

        path.append(tuple(position))
    return path


def lengths(wire):
    return [int(move[1:]) for move in wire]


def is_intersect(segment1, segment2):
    return (
        max(segment1[0][0], segment1[1][0]) >= min(segment2[0][0], segment2[1][0])
        and max(segment1[0][1], segment1[1][1]) >= min(segment2[0][1], segment2[1][1])
        and max(segment2[0][0], segment2[1][0]) >= min(segment1[0][0], segment1[1][0])
        and max(segment2[0][1], segment2[1][1]) >= min(segment1[0][1], segment1[1][1])
    )


def min_distance(segment1, segment2):
    # minimum Manhattan distance of intersection
    x_values = [segment1[0][0], segment1[1][0], segment2[0][0], segment2[1][0]]
    x_values.sort()
    x_distance = min(abs(x_values[1]), abs(x_values[2]))
    y_values = [segment1[0][1], segment1[1][1], segment2[0][1], segment2[1][1]]
    y_values.sort()
    y_distance = min(abs(y_values[1]), abs(y_values[2]))
    return x_distance + y_distance


def min_distance_path(path1, path2):
    distance = 999999
    for i in range(len(path1) - 1):
        for j in range(len(path2) - 1):
            segment1 = [path1[i], path1[i + 1]]
            segment2 = [path2[j], path2[j + 1]]
            if (
                is_intersect(segment1, segment2)
                and min_distance(segment1, segment2) < distance
                and min_distance(segment1, segment2) > 0
            ):
                distance = min_distance(segment1, segment2)

    return distance


path1 = parse(wire1)
path2 = parse(wire2)
distance = min_distance_path(path1, path2)
print("Part One:", distance)


def min_travel(segment1, segment2):
    # minimum combined steps of intersection
    x_values = [segment1[0][0], segment1[1][0], segment2[0][0], segment2[1][0]]
    x_values.sort()
    assert x_values[1] == x_values[2]
    y_values = [segment1[0][1], segment1[1][1], segment2[0][1], segment2[1][1]]
    y_values.sort()
    assert y_values[1] == y_values[2]

    return (
        abs(segment1[0][0] - x_values[1])
        + abs(segment1[0][1] - y_values[1])
        + abs(segment2[0][0] - x_values[1])
        + abs(segment2[0][1] - y_values[1])
    )


def min_travel_path(path1, path2, lengths1, lengths2):
    distance = 999999
    lengths1.insert(0, 0)
    lengths2.insert(0, 0)
    cumsum1 = np.cumsum(lengths1)
    cumsum2 = np.cumsum(lengths2)
    for i in range(len(path1) - 1):
        for j in range(len(path2) - 1):
            segment1 = [path1[i], path1[i + 1]]
            segment2 = [path2[j], path2[j + 1]]

            if is_intersect(segment1, segment2):
                travel = cumsum1[i] + cumsum2[j] + min_travel(segment1, segment2)
                if travel < distance and travel > 0:
                    distance = travel

    return distance


lengths1 = lengths(wire1)
lengths2 = lengths(wire2)
distance = min_travel_path(path1, path2, lengths1, lengths2)
print("Part Two:", distance)
