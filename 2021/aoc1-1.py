from inputs.aoc1_1_input import input


def run():
    # Count the number of times a depth measurement increases from the previous measurement.
    # (There is no measurement before the first measurement.)
    num_times_measurement_increases = 0
    for i in range(1, len(input)):
        if input[i] > input[i-1]:
            num_times_measurement_increases += 1

    print(num_times_measurement_increases)


if __name__ == "__main__":
    run()
