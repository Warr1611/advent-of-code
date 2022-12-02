import heapq
import os

def run():
    # Create a list, each entry being the total calories carried by an elf
    elf_calories = []
    total_calories = 0
    file_dir = os.path.dirname(os.path.abspath(__file__))
    # Open the file and parse each line
    with open(os.path.join(file_dir, "inputs\\aoc1_1_input.txt"),'r') as file:
        for line in file:
            line = line.strip()
            # If line is blank, set list[index] = total_calories, then reset total_calories to start the next elf
            if len(line) < 1:
                elf_calories.append(total_calories)
                total_calories = 0
                continue
            # Else, convert the contents of the line into an int and add it to the current elf's total number of calories
            else:
                total_calories = total_calories + int(line)
    print(sum(heapq.nlargest(3, elf_calories)))


if __name__ == "__main__":
    run()
