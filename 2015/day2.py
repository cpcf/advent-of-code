import sys

input = open(sys.argv[1], "r").read().splitlines()
parcels = list(map(sorted, [[int(value) for value in line.split("x")] for line in input]))

print("Part1: " + str(sum(2*l*w + 2*w*h + 2*h*l + l*w for l, w, h in parcels)))
print("Part2: " + str(sum(2*l + 2*w + l*w*h for l, w, h in parcels)))
