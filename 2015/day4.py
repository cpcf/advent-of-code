import hashlib
import sys


def find_hash_that_starts_with_target(input, target):
    i = 0
    run = True
    while run:
        hash = hashlib.md5(bytes(input.strip() + str(i), encoding='utf-8'))
        answer = hash.hexdigest()[:len(target)]
        if answer == target:
            return i
        else:
            i += 1


input = open(sys.argv[1], "r").read()

print("Part 1: " + str(find_hash_that_starts_with_target(input, '00000')))
print("Part 2: " + str(find_hash_that_starts_with_target(input, '000000')))
