import numpy
import sys


def build_rocks(input):
    rocks = set()
    base = 0
    for line in input:
        positions = [[int(i) for i in x.strip().split(',')]
                     for x in line.split('->')]
        for i, position in enumerate(positions):
            if i > 0:
                x, y = position
                last_x, last_y = positions[i - 1]
                dx = x - last_x
                dy = y - last_y
                length = abs(dx) if dx != 0 else abs(dy)
                for i in range(length + 1):
                    rock_x = last_x + (i * numpy.sign(dx))
                    rock_y = last_y + (i * numpy.sign(dy))
                    rocks.add((rock_x, rock_y))
                    base = rock_y if rock_y > base else base
    return rocks, base


def add_floor(rocks, base):
    floor = base + 2
    infinity = 150
    low = min(rock[0] for rock in rocks) - infinity
    high = max(rock[0] for rock in rocks) + infinity
    for x in range(low, high):
        rocks.add((x, floor))
    return rocks


def drop_sand(rocks, base):
    for count in range(1000000):
        sand = (500, 0)
        while True:
            if sand[1] >= base + 3:
                return(count)
            if (sand[0], sand[1] + 1) not in rocks:
                sand = (sand[0], sand[1] + 1)
            elif (sand[0] - 1, sand[1] + 1) not in rocks:
                sand = (sand[0] - 1, sand[1] + 1)
            elif (sand[0] + 1, sand[1] + 1) not in rocks:
                sand = (sand[0] + 1, sand[1] + 1)
            else:
                break
        if sand == (500, 0):
            return(count + 1)
        rocks.add(sand)


input = open(sys.argv[1], "r").readlines()
rocks, base = build_rocks(input)
print(f"Part 1: {drop_sand(rocks, base)}")
rocks, base = build_rocks(input)
print(f"Part 2: {drop_sand(add_floor(rocks, base), base)}")
