import sys


def find_unique_window(input, window_size):
    for i in range(len(input) - window_size + 1):
        if len(set(input[i: i + window_size])) == window_size:
            return i + window_size


input = open(sys.argv[1], "r").read()
print("Part 1: " + str(find_unique_window(input, 4)))
print("Part 1: " + str(find_unique_window(input, 12)))
