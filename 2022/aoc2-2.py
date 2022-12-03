import os


def run():
    strategy = []
    file_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(file_dir, "inputs\\aoc2_1_input.txt"), "r") as file:
        for line in file:
            line = line.strip()
            strategy.append([line[0], line[2]])
    heuristic = [["A", "B", "C"], ["X", "Y", "Z"]]  # In order of R,P,S
    print(score_strategy(strategy, heuristic))


def score_strategy(strategy, heuristic):
    round_scores = []
    for round in strategy:
        round_score = 0

        if round[1] == heuristic[1][0]:  # lose
            round_score = round_score + 0
        elif round[1] == heuristic[1][1]:  # tie
            round_score = round_score + 3
        elif round[1] == heuristic[1][2]:  # win
            round_score = round_score + 6

        for i in range(0, 3):
            if round[0] == heuristic[0][i]:
                if round[1] == heuristic[1][0]:  # lose
                    round_score = round_score + ((i + 2) % 3) + 1
                elif round[1] == heuristic[1][1]:  # tie
                    round_score = round_score + i + 1
                elif round[1] == heuristic[1][2]:  # win
                    round_score = round_score + ((i + 1) % 3) + 1
        round_scores.append(round_score)
    return sum(round_scores)


if __name__ == "__main__":
    run()
