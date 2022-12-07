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
        b1 = None
        b2 = None
        b3 = None
        count = 0
        for line in file:
            count = count + 1
            line = line.strip()
            if (count == 3):
                count = 0
                b3 = line
                common = ''.join(sorted(set.intersection(set(b1), set(b2), set(b3))))
                sum_priorties = sum_priorties + priorities.index(common) + 1
            elif (count == 2):
                b2 = line
            elif (count == 1):
                b1 = line
    print(sum_priorties)


if __name__ == "__main__":
    run()
