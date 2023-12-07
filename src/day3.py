import re

from collections import defaultdict
from utils import read_input_for_day


def is_part_symbol(c):
    return not c.isdigit() and c != '.'


def is_part_digit(lines, i, j):
    not_top = i > 0
    not_bot = i < len(lines) - 1
    not_left = j > 0
    not_right = j < len(lines[0]) - 1

    if not_top:
        if not_left:
            if is_part_symbol(lines[i-1][j-1]):
                return True
        if not_right:
            if is_part_symbol(lines[i-1][j+1]):
                return True
        if is_part_symbol(lines[i-1][j]):
            return True

    if not_bot:
        if not_left:
            if is_part_symbol(lines[i+1][j-1]):
                return True
        if not_right:
            if is_part_symbol(lines[i+1][j+1]):
                return True
        if is_part_symbol(lines[i+1][j]):
            return True

    if not_left:
        if is_part_symbol(lines[i][j-1]):
            return True
    if not_right:
        if is_part_symbol(lines[i][j+1]):
            return True

    return False


def part1():
    lines = read_input_for_day(3)
    lines = [list(l) for l in lines]

    output = 0
    for i in range(len(lines)):
        number = ""
        is_part = False
        for j in range(len(lines[0])):
            c = lines[i][j]

            if c.isdigit():
                number += c
                if not is_part:
                    is_part = is_part_digit(lines, i, j)
            elif number:
                if is_part:
                    output += int(number)
                number = ""
                is_part = False

        if number:
            if is_part:
                output += int(number)
            number = ""
            is_part = False

    return output


def get_gear_coordinates(lines, i, j):
    gear_coordinates = []

    not_top = i > 0
    not_bot = i < len(lines) - 1
    not_left = j > 0
    not_right = j < len(lines[0]) - 1

    if not_top:
        if not_left:
            if lines[i-1][j-1] == '*':
                gear_coordinates.append((i-1, j-1))
        if not_right:
            if lines[i-1][j+1] == '*':
                gear_coordinates.append((i-1, j+1))
        if lines[i-1][j] == '*':
            gear_coordinates.append((i-1, j))

    if not_bot:
        if not_left:
            if lines[i+1][j-1] == '*':
                gear_coordinates.append((i+1, j-1))
        if not_right:
            if lines[i+1][j+1] == '*':
                gear_coordinates.append((i+1, j+1))
        if lines[i+1][j] == '*':
            gear_coordinates.append((i+1, j))

    if not_left:
        if lines[i][j-1] == '*':
            gear_coordinates.append((i, j-1))
    if not_right:
        if lines[i][j+1] == '*':
            gear_coordinates.append((i, j+1))

    return gear_coordinates


def part2():
    lines = read_input_for_day(3)

    gear_numbers = defaultdict(list)
    for i in range(len(lines)):
        number = ""
        is_part = False
        gears = set()
        for j in range(len(lines[0])):
            c = lines[i][j]

            if c.isdigit():
                number += c
                gears.update(get_gear_coordinates(lines, i, j))
                if not is_part:
                    is_part = is_part_digit(lines, i, j)
            elif number:
                if is_part:
                    for gear in gears:
                        gear_numbers[gear].append(int(number))
                number = ""
                is_part = False
                gears = set()

        if number:
            if is_part:
                for gear in gears:
                    gear_numbers[gear].append(int(number))
            number = ""
            is_part = False
            gears = set()

    output = 0
    for gear_parts in gear_numbers.values():
        if len(gear_parts) == 2:
            output += (gear_parts[0] * gear_parts[1])

    return output


if __name__ == "__main__":
    print(part1())
    print(part2())
