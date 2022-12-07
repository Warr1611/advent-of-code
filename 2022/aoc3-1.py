import os


day_num = 3
puzzle_num = 1
priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def run():
    # Create a list, each entry being the total calories carried by an elf
    sum_priorties = 0
    file_dir = os.path.dirname(os.path.abspath(__file__))
    # Open the file and parse each line
    with open(os.path.join(file_dir, f"inputs\\aoc{day_num}_{puzzle_num}_input.txt"), "r") as file:
        for line in file:
            line = line.strip()
            length = int(len(line)/2)
            r1 = line[0:length]
            r2 = line[length:]
            common = ''.join(sorted(set.intersection(set(r1), set(r2))))
            sum_priorties = sum_priorties + priorities.index(common) + 1
    print(sum_priorties)


if __name__ == "__main__":
    run()
