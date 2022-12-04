import sys

PRIORITY = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def part1(input):
  total = 0
  for line in input:
    first_compartment, second_compartment = line[:len(line)//2], line[len(line)//2:]
    total += PRIORITY.index(''.join(set(first_compartment).intersection(second_compartment)))
  return total

def part2(input):
  total = 0
  groups = [input[i * 3:(i + 1) * 3] for i in range((len(input) + 3 - 1) // 3 )]
  for group in groups:
      total += PRIORITY.index(''.join(set(''.join(set(group[1]).intersection(group[2]))).intersection(group[0])))
  return total

input = open(sys.argv[1], "r").read().splitlines()
print("Part1: " + str(part1(input)))
print("Part2: " + str(part2(input)))
