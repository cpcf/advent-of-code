import sys

input = open(sys.argv[1], "r").read().splitlines()

elf = []
totals = []

for line in input:
  if not line:
    totals.append(sum(calories for calories in elf))
    elf = []
  else:
    elf.append(int(line))

totals.append(sum(calories for calories in elf))
totals.sort()

most = totals.pop()
print("Part1:")
print(most)

print("Part2:")
print(most + totals.pop() + totals.pop())
