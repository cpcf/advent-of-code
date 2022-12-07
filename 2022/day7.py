import sys


def build_dir_sizes(input):
    cwd = ["/"]
    dirs = {}
    for line in input.split("\n"):
        if line.startswith("$ cd"):
            next_dir = line.split()[2]
            if next_dir == "..":
                cwd.pop()
            elif next_dir != "/":
                if len(cwd) == 1:
                    cwd.append('/' + next_dir)
                else:
                    cwd.append(cwd[-1] + '/' + next_dir)
        elif line[0].isnumeric():
            for dir in cwd:
                if dir not in dirs:
                    dirs[dir] = 0
                dirs[dir] += int(line.split()[0])
    return dirs


def part1(dirs):
    return sum(size for size in dirs.values()
               if size <= 100000)


def part2(dirs):
    required_space = 30000000 + dirs['/'] - 70000000
    return min(size for size in dirs.values()
               if size >= required_space)


input = open(sys.argv[1], "r").read()
dirs = build_dir_sizes(input)

print("Part 1: " + str(part1(dirs)))
print("Part 2: " + str(part2(dirs)))
