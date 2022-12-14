import sys
import ast

ORDER = {
    'incorrect': 0,
    'correct': 1,
    'neither': 2
}


def convert_pairs(packets):
    packet1, packet2 = packets.splitlines()
    return [ast.literal_eval(packet1), ast.literal_eval(packet2)]


def compare_ints(left, right):
    if left < right:
        return ORDER['correct']
    if left > right:
        return ORDER['incorrect']
    if left == right:
        return ORDER['neither']


def are_lists_in_correct_order(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return compare_ints(left, right)
    elif isinstance(left, int):
        return compare_list([left], right)
    elif isinstance(right, int):
        return compare_list(left, [right])
    else:
        return compare_list(left, right)


def compare_list(left, right):
    left_length = len(left)
    right_length = len(right)
    i = 0
    while(True):
        if i == left_length == right_length:
            return ORDER['neither']
        elif i == left_length:
            return ORDER['correct']
        elif i == right_length:
            return ORDER['incorrect']
        correct_order = are_lists_in_correct_order(left[i], right[i])
        if correct_order is not ORDER['neither']:
            return correct_order
        i += 1


def packet_sort(packets):
    packets_length = [*range(0, len(packets), 1)]
    reversed_range = list(reversed(packets_length))
    for i in packets_length:
        for j in range(0, reversed_range[i]):
            if compare_list(packets[j], packets[j + 1]) == ORDER['incorrect']:
                packets[j], packets[j + 1] = packets[j + 1], packets[j]
    return packets


def part1(input):
    data = input.split("\n\n")
    packet_pairs = [[pair for pair in convert_pairs(chunk)] for chunk in data]
    answer = 0
    for count, packets in enumerate(packet_pairs):
        if compare_list(packets[0], packets[1]) == ORDER['correct']:
            answer += count + 1
    return answer


def part2(input):
    data = input.splitlines()
    packets = []
    for line in data:
        if line:
            packets.append(ast.literal_eval(line))
    packets.append([[2]])
    packets.append([[6]])
    packets = packet_sort(packets)
    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


input = open(sys.argv[1], "r").read()
print(f"Part 1: {part1(input)}")
print(f"Part 2: {part2(input)}")
