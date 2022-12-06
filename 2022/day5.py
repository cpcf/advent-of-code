import copy
import sys


def build_initial_crate_layout(crate_layout_input, crate_labels):
    crate_layout = []
    for layer in crate_layout_input:
        columns = layer[1::4]
        for index in range(len(columns)):
            if len(crate_layout) <= index:
                crate_layout.append([])
            crate = columns[index]
            if not crate.isspace():
                crate_layout[index].append(crate)
    return crate_layout


def convert_instructions(instructions):
    return [list(map(int, line.split()[1::2]))for line in instructions]


def prepare_input(input):
    blank = input.index('')
    crates = input[:blank]
    instructions = input[blank + 1:]
    crate_layout = build_initial_crate_layout(crates, crates.pop())
    converted_instructions = convert_instructions(instructions)
    return crate_layout, converted_instructions


def apply_instructions_cratemover_9000(crates, converted_instructions):
    for instruction in converted_instructions:
        amount_to_move, move_from, move_to = instruction
        for i in range(amount_to_move):
            crates[move_to - 1].insert(0, crates[move_from - 1].pop(0))
    return crates


def apply_instructions_cratemover_9001(crates, converted_instructions):
    for instruction in converted_instructions:
        amount_to_move, move_from, move_to = instruction
        crates_on_the_move = crates[move_from - 1][0:amount_to_move]
        del crates[move_from - 1][0:amount_to_move]
        while crates_on_the_move:
            crates[move_to - 1].insert(0, crates_on_the_move.pop())
    return crates


def get_top_layer(resulting_crates):
    top_crates = []
    for column in resulting_crates:
        if column:
            top_crates.append(column.pop(0))
    return ''.join(top_crates)


input = open(sys.argv[1], "r").read().splitlines()
crates, converted_instructions = prepare_input(input)

print('Part1: ' + get_top_layer(apply_instructions_cratemover_9000(
      copy.deepcopy(crates), converted_instructions)))
print('Part2: ' + get_top_layer(apply_instructions_cratemover_9001(
      copy.deepcopy(crates), converted_instructions)))
