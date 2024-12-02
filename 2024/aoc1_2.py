import os


def measure_error(left, counts):
    s = 0
    for i in range(len(left)):
        s = s + (left[i] * counts.get(left[i], 0))
    print(s)


def run():
    left_list = []
    right_list = []
    counts = {}
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
            counts[r] = counts.get(r, 0) + 1
    measure_error(left_list, counts)


if __name__ == "__main__":
    run()