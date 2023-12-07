import re
from utils import read_input


def part1():
    lines = read_input("day1.txt")
    output = 0
    for line in lines:
        first_digit = re.search(r"\d", line).group(0)
        last_digit = re.search(r"\d", line[::-1]).group(0)
        output += int(first_digit + last_digit)
    return output

def part2():
    lines = read_input("day1.txt")
    digits = {
        '0': '0',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        "zero": '0',
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9'
    }
    backward_digits = {
        digit_txt[::-1]: digit for digit_txt, digit in digits.items()
    }

    print(backward_digits)

    output = 0
    for line in lines:
        print(line)
        first_digit = ""
        first_pos = float("inf")
        for digit_txt, digit in digits.items():
            if (pos := line.find(digit_txt)) > -1 and pos < first_pos:
                first_digit = digit
                first_pos = pos

        backward_line = line[::-1]
        last_digit = ""
        last_pos = float("inf")
        for digit_txt, digit in backward_digits.items():
            if (pos := backward_line.find(digit_txt)) > -1 and pos < last_pos:
                last_digit = digit
                last_pos = pos

        output += int(first_digit + last_digit)

        print(first_digit, last_digit)

    return output


if __name__ == "__main__":
    print(part1())
    print(part2())
