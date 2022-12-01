from inputs.aoc3_1_input import input


def run():
    ones = [0]*len(input[0])
    half = int(len(input) / 2.0)

    for line in input:
        for i in range(0, len(line)):
            if line[i] == '1':
                ones[i] += 1

    oxygen_input = input.copy()
    indices_to_keep = [i for i in range(0, len(oxygen_input))]
    for i in range(0, len(ones)):
        for oi in range(0, len(oxygen_input)):
            if (oi in indices_to_keep) and ((ones[i] < half and oxygen_input[oi][i] == '1') or (ones[i] >= half and oxygen_input[oi][i] == '0')):
                indices_to_keep.remove(oi)
        if len(indices_to_keep) == 1:
            break
    oxygen_input = [oxygen_input[i] for i in indices_to_keep]
    
    c02_input = input.copy()
    indices_to_keep = [i for i in range(0, len(c02_input))]
    for i in range(0, len(ones)):
        for oi in range(0, len(c02_input)):
            if (oi in indices_to_keep) and ((ones[i] >= half and c02_input[oi][i] == '1') or (ones[i] < half and c02_input[oi][i] == '0')):
                indices_to_keep.remove(oi)
        if len(indices_to_keep) == 1:
            break
    c02_input = [c02_input[i] for i in indices_to_keep]

    o2_dec = int(oxygen_input[0], 2)
    c02_dec = int(c02_input[0], 2)

    print(o2_dec * c02_dec)


if __name__ == "__main__":
    run()
