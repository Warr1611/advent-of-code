from inputs.aoc2_1_input import input


def parse_directions(line):
    return line.split(" ")


def run():
    horizontal = 0
    depth = 0

    for line in input:
        direction, amount = parse_directions(line)
        amount = int(amount)
        if direction == "forward":
            horizontal += amount
        elif direction == "up":
            depth -= amount
        elif direction == "down":
            depth += amount

    print(horizontal * depth)


if __name__ == "__main__":
    run()
