def build_ranges(line):
  first_elf, second_elf = line.split(",")
  first_elf_low, first_elf_high = first_elf.split("-")
  second_elf_low, second_elf_high = second_elf.split("-")
  first_elf_range = range(int(first_elf_low), int(first_elf_high) + 1)
  second_elf_range = range(int(second_elf_low), int(second_elf_high) + 1)
  return first_elf_range, second_elf_range

input = open("input.txt", "r").read().splitlines()

total1 = 0
total2 = 0

for line in input:
  first_elf_range, second_elf_range = build_ranges(line)
  if (first_elf_range[0] in second_elf_range and first_elf_range[-1] in second_elf_range) or (second_elf_range[0] in first_elf_range and second_elf_range[-1] in first_elf_range):
    total1 += 1
  if len(range(max(first_elf_range[0], second_elf_range[0]), min(first_elf_range[-1], second_elf_range[-1])+1)) > 0:
    total2 += 1

print("Part1: " + str(total1))
print("Part2: " + str(total2))
