import sys
import numpy


class Monkey:
    def __init__(self, index, items, operation, test, if_true, if_false):
        self.index = index
        self.items = items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.count = 0
        self.lcm = 0

    def take_item(self):
        self.items.pop(0)

    def recieve_item(self, item):
        self.items.append(item)

    def inspect(self, item, divide_by_three):
        self.count += 1
        arg = item if not self.operation[1] else self.operation[1]
        if self.operation[0] == '+':
            item += arg
        else:
            item *= arg
        if divide_by_three:
            return item // 3
        else:
            # returning the modulus of the lcm to keep the items small
            # while maintaining remainder
            return item % self.lcm

    def target(self, item):
        return self.if_true if item % self.test == 0 else self.if_false


def parse_monkeys(input):
    monkeys = []
    index = 0
    items = []
    operation = (0, 0)
    test = 0
    if_true = 0
    if_false = 0
    for line in input:
        if not line:
            monkey = Monkey(index, items, operation, test, if_true, if_false)
            monkeys.append(monkey)
            continue
        tokens = line.strip().split()
        if tokens[0] == 'Monkey':
            index = tokens[1][:-1]
        elif tokens[0] == 'Starting':
            items = [int(item.replace(',', ' ')) for item in tokens[2:]]
        elif tokens[0] == 'Operation:':
            arg = int(tokens[-1]) if tokens[-1].isnumeric() else None
            operation = (tokens[-2], arg)
        elif tokens[0] == 'Test:':
            test = int(tokens[-1])
        elif tokens[0] == 'If':
            if tokens[1] == 'true:':
                if_true = int(tokens[-1])
            else:
                if_false = int(tokens[-1])
    monkey = Monkey(index, items, operation, test, if_true, if_false)
    monkeys.append(monkey)
    lcm = numpy.lcm.reduce([monkey.test for monkey in monkeys])
    for monkey in monkeys:
        monkey.lcm = lcm
    return monkeys


def run(input, rounds, divide_by_three):
    monkeys = parse_monkeys(input)
    for _ in range(rounds):
        for monkey in monkeys:
            while monkey.items:
                item = monkey.inspect(monkey.items.pop(0), divide_by_three)
                monkeys[monkey.target(item)].recieve_item(item)
    counts = sorted([monkey.count for monkey in monkeys])
    return(counts[-1] * counts[-2])


input = open(sys.argv[1], "r").read().splitlines()
print(f"Part1: {run(input, 20, True)}")
print(f"Part2: {run(input, 10_000, False)}")
