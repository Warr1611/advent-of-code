from collections import deque
import os
import re


day_num = 5
puzzle_num = 1


stacks_map = {
    1: deque(['N', 'R', 'J', 'T', 'Z', 'B', 'D', 'F']),
    2: deque(['H', 'J', 'N', 'S', 'R']),
    3: deque(['Q', 'F', 'Z', 'G', 'J', 'N', 'R', 'C']),
    4: deque(['Q', 'T', 'R', 'G', 'N', 'V', 'F']),
    5: deque(['F', 'Q', 'T', 'L']),
    6: deque(['N', 'G', 'R', 'B', 'Z', 'W', 'C', 'Q']),
    7: deque(['M', 'H', 'N', 'S', 'L', 'C', 'F']),
    8: deque(['J', 'T', 'M', 'Q', 'N', 'D']),
    9: deque(['S', 'G', 'P']),
}


def run():
    # Create a list, each entry being the total calories carried by an elf
    stack_tops = ''
    file_dir = os.path.dirname(os.path.abspath(__file__))
    # Open the file and parse each line
    with open(os.path.join(file_dir, f"inputs\\aoc{day_num}_{puzzle_num}_input.txt"), "r") as file:
        moves = []
        for line in file:
            line = line.strip()
            move = re.split('move | from | to ', line)
            moves.append([int(move[1]), int(move[2]), int(move[3])])

    for move in moves:
        for move_num in range(0, move[0]):
            from_stack = stacks_map[move[1]]
            to_stack = stacks_map[move[2]]

            to_stack.appendleft(from_stack.popleft())

    for i in range(0, len(stacks_map)):
        stack_tops = stack_tops + stacks_map[i+1].popleft()

    print(stack_tops)


if __name__ == "__main__":
    run()
