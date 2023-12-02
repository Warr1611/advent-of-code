import os


def get_calibration_value(line):
    first_digit = None
    last_digit = None
    line_len = len(line)
    for i in range(line_len):
        if line[i].isdigit():
            first_digit = line[i]
            break
    for i in range(line_len):
        if line[line_len - i - 1].isdigit():
            last_digit = line[line_len - i - 1]
            break
    return int(f"{first_digit}{last_digit}")


def run():
    # Create a list, each entry being the total calories carried by an elf
    calibration_values = []
    calibration_sum = 0
    file_dir = os.path.dirname(os.path.abspath(__file__))
    # Open the file and parse each line
    with open(os.path.join(file_dir, "inputs\\aoc1_1_input.txt"), "r") as file:
        for line in file:
            line = line.strip()
            val = get_calibration_value(line)
            calibration_sum = calibration_sum + val
    print(calibration_sum)


if __name__ == "__main__":
    run()
