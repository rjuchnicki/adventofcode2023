import re

from utils import read_input_for_day


DAY = 6
lines = read_input_for_day(DAY)
times = [int(t) for t in re.findall(r"\d+", lines[0])]
distances = [int(d) for d in re.findall(r"\d+", lines[1])]

def num_ways_to_win(duration: int, distance: int):
    wins = 0
    for hold_duration in range(duration + 1):
        if hold_duration * (duration - hold_duration) > distance:
            wins += 1
    return wins

def part1():
    output = 1
    for i in range(len(times)):
        output *= num_ways_to_win(times[i], distances[i])

    return output


def part2():
    time = int("".join(str(t) for t in times))
    distance = int("".join([str(d) for d in distances]))

    return num_ways_to_win(time, distance)


if __name__ == "__main__":
    print(part1())
    print(part2())
