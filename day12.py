import sys


def parse_input():
    grid = {}
    for y, line in enumerate(open(sys.argv[1]).readlines()):
        for x, height in enumerate(line.strip()):
            grid[(x, y)] = height
    return grid


def target_within_one(position, target):
    position_height = ord(grid[position].replace("S", "a"))
    target_height = ord(grid[target].replace("E", 'z'))
    return target_height - position_height <= 1


def possible_neighbours(position, grid):
    x, y = position
    neighbours = []
    for target in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if target in grid and target_within_one(position, target):
            neighbours.append(target)
    return neighbours


def walk(distance, layers, grid):
    step = set(target for position in layers[-1]
               for target in possible_neighbours(position, grid)
               if target not in distance)
    distance.update({position: len(layers) for position in step})
    if step:
        walk(distance, layers + [step], grid)


def find_distance(start, end, grid):
    distance = {start: 0}
    walk(distance, [{start}], grid)
    return distance[end] if end in distance else None


def find_positions(values, grid):
    return list(position for (position, v) in grid.items() if v in values)


def part1(grid):
    start = find_positions("S", grid)[0]
    end = find_positions("E", grid)[0]
    return find_distance(start, end, grid)


def part2(grid):
    distances = []
    for start in find_positions(["S", "a"], grid):
        distance = find_distance(start, find_positions("E", grid)[0], grid)
        if distance:
            distances.append(distance)
    return min(distances)


grid = parse_input()

print(f'Part 1: {part1(grid)}')
print(f'Part 2: {part2(grid)}')
