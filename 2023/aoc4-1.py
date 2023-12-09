import os
import math


def parse_game_data(line):
    winning_list, played_list = line.replace("  ", " ").split(":")[1].split("|")
    winning = winning_list.strip().split(" ")
    played = played_list.strip().split(" ")
    worth = 0
    for p in played:
        if p in winning:
            if worth == 0:
                worth = 1
            else:
                worth = worth * 2
    return worth


def run():
    worth_sum = 0
    file_dir = os.path.dirname(os.path.abspath(__file__))
    # Open the file and parse each line
    with open(os.path.join(file_dir, "inputs\\aoc4_1_input.txt"), "r") as file:
        for line in file:
            line = line.strip()
            worth = parse_game_data(line)
            worth_sum = worth_sum + worth

    print(worth_sum)


if __name__ == "__main__":
    run()
