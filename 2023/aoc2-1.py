import os
import math

possible_cubes = {
    # 12 red cubes, 13 green cubes, and 14 blue cubes
    "red": 12,
    "green": 13,
    "blue": 14,
}


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


def validate_game_data(game_data):
    for color, cubes in game_data.items():
        if color not in possible_cubes.keys():
            return False
        if not possible_cubes.get(color, math.inf) >= cubes:
            return False
    return True


def run():
    possible_game_sum = 0
    file_dir = os.path.dirname(os.path.abspath(__file__))
    # Open the file and parse each line
    with open(os.path.join(file_dir, "inputs\\aoc2_1_input.txt"), "r") as file:
        for line in file:
            line = line.strip()
            id, game_data = parse_game_data(line)
            if validate_game_data(game_data):
                possible_game_sum = possible_game_sum + int(id)

    print(possible_game_sum)


if __name__ == "__main__":
    run()
