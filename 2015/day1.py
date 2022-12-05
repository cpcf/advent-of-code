import sys

def part2(input):
  floor = 0
  count = 0
  for char in input:
    if char == "(":
    	floor += 1
    else:
      floor -= 1
    count += 1
    if floor == -1:
    	return str(count)

input = open(sys.argv[1], "r").read()
print("Part1: " + str(input.count('(') - input.count(')')))
print("Part2: " + part2(input))
