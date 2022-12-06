import sys

PRIORITY = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def part1(input):
    total = 0
    for line in input:
        total += PRIORITY.index(''.join(set(line[:len(line) // 2])
                                        & set(line[len(line) // 2:])))
    return total


def part2(input):
    total = 0
    groups = [input[i * 3:(i + 1) * 3]
              for i in range((len(input) + 3 - 1) // 3)]
    for group in groups:
        total += PRIORITY.index(''.join(set(group[0])
                                        & set(group[1]) & set(group[2])))
    return total


input = open(sys.argv[1], "r").read().splitlines()
print("Part1: " + str(part1(input)))
print("Part2: " + str(part2(input)))
