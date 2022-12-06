import sys

input = open(sys.argv[1], "r").read().splitlines()
parcels = list(map(sorted, [[int(value)
                             for value in line.split("x")] for line in input]))

print("Part1: " + str(sum(2 * length * width
                          + 2 * width * height
                          + 2 * height * length
                          + length * width for
                          length, width, height in parcels)))
print("Part2: " + str(sum(2 * length
                          + 2 * width
                          + length * width * height for
                          length, width, height in parcels)))
