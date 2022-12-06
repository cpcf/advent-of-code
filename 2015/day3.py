import sys


def update_houses(houses, house):
    if house in houses:
        houses[house] += 1
    else:
        houses[house] = 1


def deliver(houses, input):
    x, y = 0, 0
    update_houses(houses, (x, y))
    for move in input:
        if move == "^":
            y += 1
        elif move == "v":
            y -= 1
        elif move == ">":
            x += 1
        elif move == "<":
            x -= 1
        update_houses(houses, (x, y))
    return houses


input = open(sys.argv[1], "r").read()
print("Part 1: " + str(len(deliver({}, input))))
print("Part 2: " + str(len(deliver(deliver({}, input[::2]), input[1::2]))))
