import re
import sys

bad_strings = re.compile(r'ab|cd|pq|xy')
vowels = re.compile(r'[aeiou]')
pair_appears_twice = re.compile(r'(\w{2}).*\1')


def contains_bad_string(string):
    return bad_strings.search(string)


def has_three_vowels(string):
    return len(vowels.findall(string)) >= 3


def has_any_repeated_chars(string):
    previous = ''
    for letter in string:
        if letter == previous:
            return True
        else:
            previous = letter
    return False


def is_good_string_part1(string):
    return \
        not contains_bad_string(string) \
        and has_three_vowels(string) \
        and has_any_repeated_chars(string)


def does_pair_appear_twice(string):
    return pair_appears_twice.search(string)


def letter_twice_with_one_letter_between(string):
    for i in range(len(string) - 2):
        if string[i] is string[i + 2]:
            return True
    return False


def is_good_string_part2(string):
    return \
        does_pair_appear_twice(string) \
        and letter_twice_with_one_letter_between(string)


input = open(sys.argv[1], "r").read().splitlines()
print("Part 1: " + str(len(list(filter(is_good_string_part1, input)))))
print("Part 2: " + str(len(list(filter(is_good_string_part2, input)))))
