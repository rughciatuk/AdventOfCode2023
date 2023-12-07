def parse(lines):
    board = []
    for line in lines:
        # first we remove the game part
        line = line.split(": ")[1]
        # split for the winning number and my numbers
        winning_numbers, my_numbers = line.split("| ")
        winning_numbers = [
            int(x.strip()) for x in winning_numbers.strip().split(" ") if x
        ]
        my_numbers = [int(x.strip()) for x in my_numbers.strip().split(" ") if x]
        board.append((winning_numbers, my_numbers))
    return board


def calc_wins(winning_numbers, my_numbers):
    wins = 0
    for num in my_numbers:
        if num in winning_numbers:
            wins += 1
    return wins


def calc_value(wins):
    if wins == 0:
        return 0
    elif wins == 1:
        return 1
    else:
        return 2 ** (wins - 1)


def calc_board(board):
    game_values = [1 for _ in range(len(board))]
    for index, values in enumerate(board):
        winning_numbers, my_numbers = values
        wins = calc_wins(winning_numbers, my_numbers)
        if wins > 0:
            for i in range(index + 1, index + wins + 1):
                game_values[i] += game_values[index]
    return sum(game_values)


def main():
    with open("../input", "r") as f:
        lines = f.readlines()

    board = parse(lines)
    print(calc_board(board))


if __name__ == "__main__":
    main()
