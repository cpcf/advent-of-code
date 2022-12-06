import sys


def init_lights():
    return [[0 for i in range(1000)] for j in range(1000)]


def convert_instructions(line):
    split = line.split()
    if split[0] == "toggle":
        return (split[0],
                list(map(int, split[1].split(","))),
                list(map(int, split[-1].split(","))))
    else:
        return (split[1],
                list(map(int, split[2].split(","))),
                list(map(int, split[-1].split(","))))


def build_instructions(input):
    return list(map(convert_instructions, input))


def run_instruction_part1(instruction, lights):
    change, low, high = instruction
    for i in range(low[0] - 1, high[0]):
        for j in range(low[1] - 1, high[1]):
            if change == 'on':
                lights[i][j] = 1
            elif change == 'off':
                lights[i][j] = 0
            else:
                lights[i][j] = 1 - lights[i][j]


def run_instruction_part2(instruction, lights):
    change, low, high = instruction
    for i in range(low[0] - 1, high[0]):
        for j in range(low[1] - 1, high[1]):
            if change == 'on':
                lights[i][j] += 1
            elif change == 'toggle':
                lights[i][j] += 2
            elif change == 'off' and lights[i][j] > 0:
                lights[i][j] -= 1


def run_instructions_part1(input):
    lights = init_lights()
    instructions = build_instructions(input)
    for instruction in instructions:
        run_instruction_part1(instruction, lights)
    return sum(list(map(sum, lights)))


def run_instructions_part2(input):
    lights = init_lights()
    instructions = build_instructions(input)
    for instruction in instructions:
        run_instruction_part2(instruction, lights)
    return sum(list(map(sum, lights)))


input = open(sys.argv[1], "r").read().splitlines()

print("Part 1: " + str(run_instructions_part1(input)))
print("Part 2: " + str(run_instructions_part2(input)))
