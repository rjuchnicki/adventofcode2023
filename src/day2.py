import re

from utils import read_input_for_day


RED = 12
BLUE = 14
GREEN = 13

def part1():
    games = read_input_for_day(2)

    valid_game_id_sum = 0
    for i, game in enumerate(games, start=1):
        game = game[game.find(':') + 1:]
        rounds = game.split(';')
        valid_game = True
        for r in rounds:
            red = re.search(r"(\d+) red", r)
            red = int(red.group(1)) if red else 0
            blue = re.search(r"(\d+) blue", r)
            blue = int(blue.group(1)) if blue else 0
            green = re.search(r"(\d+) green", r)
            green = int(green.group(1)) if green else 0

            if red > RED or blue > BLUE or green > GREEN:
                valid_game = False
                break

        if valid_game:
            valid_game_id_sum += i

    return valid_game_id_sum
    

def part2():
    games = read_input_for_day(2)

    game_power_sum = 0
    for game in games:
        game = game[game.find(':') + 1:]
        rounds = game.split(';')

        min_red = 0
        min_blue = 0
        min_green = 0
        for r in rounds:
            red = re.search(r"(\d+) red", r)
            red = int(red.group(1)) if red else 0
            blue = re.search(r"(\d+) blue", r)
            blue = int(blue.group(1)) if blue else 0
            green = re.search(r"(\d+) green", r)
            green = int(green.group(1)) if green else 0

            if red > min_red:
                min_red = red
            if blue > min_blue:
                min_blue = blue
            if green > min_green:
                min_green = green

        power = min_red * min_blue * min_green
        game_power_sum += power

    return game_power_sum
 

if __name__ == "__main__":
    print(part1())
    print(part2())
