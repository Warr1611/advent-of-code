import os
import re


day_num = 4
puzzle_num = 1


def run():
    # Create a list, each entry being the total calories carried by an elf
    total_contained = 0
    file_dir = os.path.dirname(os.path.abspath(__file__))
    # Open the file and parse each line
    with open(os.path.join(file_dir, f"inputs\\aoc{day_num}_{puzzle_num}_input.txt"), "r") as file:
        for line in file:
            line = line.strip()
            ranges = re.split('-|,', line)
            r1b = int(ranges[0])
            r1e = int(ranges[1])
            r2b = int(ranges[2])
            r2e = int(ranges[3])
            if r1b >= r2b and r1b <= r2e:
                total_contained = total_contained + 1
            elif r2b >= r1b and r2b <= r1e:
                total_contained = total_contained + 1
    print(total_contained)


if __name__ == "__main__":
    run()
