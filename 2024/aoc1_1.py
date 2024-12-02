import os


def measure_error(left, right):
    l = sorted(left)
    r = sorted(right)
    s = 0
    for i in range(len(l)):
        s = s + abs(l[i] - r[i])
    print(s)


def run():
    left_list = []
    right_list = []
    file_dir = os.path.dirname(os.path.abspath(__file__))
    # Open the file and parse each line
    with open(os.path.join(file_dir, "inputs\\aoc1_1_input.txt"), "r") as file:
        for line in file:
            line = line.strip()
            line = line.split('   ')
            l = int(line[0])
            r = int(line[1])
            left_list.append(l)
            right_list.append(r)
    measure_error(left_list, right_list)


if __name__ == "__main__":
    run()