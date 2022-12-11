import sys
import numpy

MOVEMENTS = {
    'U': (0, 1),
    'D': (0, -1),
    'R': (1, 0),
    'L': (-1, 0)
}


def calculate_rope_moves(knots, input):
    head = [0, 0]
    tail_locations = {(0, 0)}
    for line in input:
        direction, count = line.split()
        dx, dy = MOVEMENTS[direction]
        for _ in range(int(count)):
            head[0] += dx
            head[1] += dy
            last_knot = head
            for i in range(len(knots)):
                next_knot = knots[i]
                if abs(next_knot[0] - last_knot[0]) > 1 \
                   or abs(next_knot[1] - last_knot[1]) > 1:
                    next_knot[0] += numpy.sign(last_knot[0] - next_knot[0])
                    next_knot[1] += numpy.sign(last_knot[1] - next_knot[1])
                last_knot = next_knot
            tail_locations.add((knots[-1][0], knots[-1][1]))
    return len(tail_locations)


input = open(sys.argv[1], "r").read().splitlines()

one_knot = [[0, 0]]
print("Part1: " + str(calculate_rope_moves(one_knot, input)))

nine_knots = [[0, 0], [0, 0], [0, 0], [0, 0],
              [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
print("Part2: " + str(calculate_rope_moves(nine_knots, input)))
