import sys


def signal_strengths(cycles, x, answer, limits):
    if limits and cycles >= limits[-1]:
        answer += limits.pop() * x
    return answer, limits


def update_pixels(cycles, x, pixels, _):
    pos = (cycles - 1) % 40
    if pos in {x - 1, x, x + 1}:
        pixels[cycles - 1] = "#"
    return pixels, None


def cpu(per_cycle_action, input, y, z):
    x = 1
    cycles = 0
    for line in input:
        instruction = line.split()
        if len(instruction) == 1:
            cycles += 1
            y, z = per_cycle_action(cycles, x, y, z)
        else:
            cycles += 1
            y, z = per_cycle_action(cycles, x, y, z)
            cycles += 1
            y, z = per_cycle_action(cycles, x, y, z)
            x += int(instruction[1])
    return y


def print_screen(input):
    screen_width = 40
    pixels = cpu(update_pixels, input, list(" " * screen_width * 6), None)
    for i in range(0, len(pixels), screen_width):
        print("".join(pixels[i: i + screen_width]))


input = open(sys.argv[1], "r").read().splitlines()

part1_answer = cpu(signal_strengths, input, 0, [220, 180, 140, 100, 60, 20])
print(f"Part1: {part1_answer}")
print("Part2: ")
print_screen(input)
