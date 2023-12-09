import os
import math


def parse_game_data(line):
    sc_index = line.find(':')
    id = line[0:sc_index].split(' ')[1]
    game_cubes = {}
    for game_segment in line[sc_index + 1:].split(';'):
        for cube_segment in game_segment.strip().split(', '):
            cubes, color = cube_segment.split(' ')
            if game_cubes.get(color, -1) < int(cubes):
                game_cubes[color] = int(cubes)
    return id, game_cubes


def get_game_power(game_data):
    power = 1
    if game_data.get("red", None) is None:
        game_data["red"] = 0
    if game_data.get("green", None) is None:
        game_data["green"] = 0
    if game_data.get("blue", None) is None:
        game_data["blue"] = 0
    for color, cubes in game_data.items():
        power = power * cubes
    return power


def run():
    power_sum = 0
    file_dir = os.path.dirname(os.path.abspath(__file__))
    # Open the file and parse each line
    with open(os.path.join(file_dir, "inputs\\aoc2_1_input.txt"), "r") as file:
        for line in file:
            line = line.strip()
            id, game_data = parse_game_data(line)
            power = get_game_power(game_data)
            power_sum = power_sum + power

    print(power_sum)


if __name__ == "__main__":
    run()
