import os


def validate(line):
    valid = 1

    if line[0] > line[1]:
        # Decreasing
        for i in range(len(line) - 1):
            if line[i] - line[i+1] > 3 or line[i] - line[i+1] < 1:
                valid = 0
                break
    else:
        # Increasing
        for i in range(len(line) - 1):
            if line[i+1] - line[i] > 3 or line[i+1] - line[i] < 1:
                valid = 0
                break

    return valid


def run():
    num_safe = 0
    file_dir = os.path.dirname(os.path.abspath(__file__))
    # Open the file and parse each line
    with open(os.path.join(file_dir, "inputs\\aoc2_1_input.txt"), "r") as file:
        for line in file:
            line = line.strip().split(' ')
            line = [int(l) for l in line]
            num_safe = num_safe + validate(line)
    print(num_safe)

if __name__ == "__main__":
    run()