import sys
import numpy as np


def is_visible_one_dir(line, height):
    return all(height > tree for tree in line)


def is_visible_ortho(line, index):
    height = line[index]
    return is_visible_one_dir(line[:index], height) \
        or is_visible_one_dir(line[index + 1:], height)


def is_visible(row, column, input_array):
    return (is_visible_ortho(input_array[row], column)) \
        or (is_visible_ortho(input_array[:, column], row))


def count_visible(input_array):
    count = 0
    for i in range(len(input_array)):
        for j in range(len(input_array[0])):
            if is_visible(i, j, input_array):
                count += 1
    return count


def scenic_score_one_direction(indices, line, height):
    score = 0
    for i in indices:
        score += 1
        if line[i] >= height:
            break
    return score


def scenic_score_line(line, index):
    height = line[index]
    return scenic_score_one_direction(range(index - 1, -1, -1), line, height) \
        * scenic_score_one_direction(range(index + 1, len(line)), line, height)


def scenic_score(row, column, input_array):
    return scenic_score_line(input_array[row], column) \
        * scenic_score_line(input_array[:, column], row)


def find_high_score(input_array):
    score = 0
    for i in range(len(input_array)):
        for j in range(len(input_array[0])):
            new_score = scenic_score(i, j, input_array)
            score = new_score if new_score > score else score
    return score


input = open(sys.argv[1], "r").read().splitlines()
input_array = np.array([[int(char) for char in row] for row in input])

print("Part1: " + str(count_visible(input_array)))
print("Part2: " + str(find_high_score(input_array)))
