from inputs.aoc3_1_input import input


def run():
    ones = [0]*len(input[0])
    gamma = [0]*len(input[0])
    epsilon = [0]*len(input[0])
    half = len(input) / 2.0

    for line in input:
        for i in range(0, len(line)):
            if line[i] == '1':
                ones[i] += 1

    for i in range(0, len(ones)):
        if ones[i] > half:
            gamma[i] = '1'
            epsilon[i] = '0'
        else:
            gamma[i] = '0'
            epsilon[i] = '1'

    gamma = ''.join(gamma)
    epsilon = ''.join(epsilon)
    gamma_dec = int(gamma, 2)
    epsilon_dec = int(epsilon, 2)

    print(gamma_dec * epsilon_dec)


if __name__ == "__main__":
    run()
