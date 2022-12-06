import sys


def build_ranges(line):
    first_elf, second_elf = line.split(",")
    first_elf_low, first_elf_high = first_elf.split("-")
    second_elf_low, second_elf_high = second_elf.split("-")
    first_elf_range = range(int(first_elf_low), int(first_elf_high) + 1)
    second_elf_range = range(int(second_elf_low), int(second_elf_high) + 1)
    return first_elf_range, second_elf_range


def contains(subset, container):
    return subset[0] in container and subset[-1] in container


def is_either_range_subset(first_range, second_range):
    return contains(first_range, second_range) \
        or contains(second_range, first_range)


input = open(sys.argv[1], "r").read().splitlines()

total1 = 0
total2 = 0

for line in input:
    first_elf_range, second_elf_range = build_ranges(line)
    if is_either_range_subset(first_elf_range, second_elf_range):
        total1 += 1
    if len(range
            (max(first_elf_range[0], second_elf_range[0]),
             min(first_elf_range[-1], second_elf_range[-1]) + 1)
           ) > 0:
        total2 += 1

print("Part1: " + str(total1))
print("Part2: " + str(total2))
