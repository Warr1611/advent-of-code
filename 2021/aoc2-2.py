from inputs.aoc2_1_input import input


def parse_directions(line):
    return line.split(" ")


def run():
    horizontal = 0
    depth = 0
    aim = 0

    for line in input:
        direction, amount = parse_directions(line)
        amount = int(amount)
        if direction == "forward":
            horizontal += amount
            depth += (aim * amount)
        elif direction == "up":
            aim -= amount
        elif direction == "down":
            aim += amount

    print(horizontal * depth)


if __name__ == "__main__":
    run()
