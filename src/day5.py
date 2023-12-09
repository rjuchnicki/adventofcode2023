import re
from utils import read_input_for_day


DAY = 5
lines = read_input_for_day(DAY)
seeds = [int(s) for s in lines[0].replace("seeds: ", "").split()]
maps = []
current_map = None
for line in lines[2:]:
    if "map" in line:
        current_map = []
        maps.append(current_map)
    elif (match := re.match(r"(\d+) (\d+) (\d+)", line)):
        # Map elements come in as: destination range start, the source range start, and the range length
        # Switch to (source, destination, length)
        current_map.append((int(match.group(2)), int(match.group(1)), int(match.group(3))))


def part1():
    current_seeds = [s for s in seeds]
    for m in maps:
        new_seeds = []
        for seed in current_seeds:
            found_match = False
            for source_start, destination_start, length in m:
                if seed >= source_start and seed <= source_start + length:
                    new_seeds.append(seed + (destination_start - source_start))
                    found_match = True
            
            if not found_match:
                new_seeds.append(seed)
        current_seeds = new_seeds

    return min(current_seeds)


def part2():
    return ""


if __name__ == "__main__":
    print(part1())
    print(part2())
