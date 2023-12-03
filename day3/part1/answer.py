class Number:
    def __init__(self, value, start_x, end_x, y):
        self.value = value
        self.start_x = start_x
        self.end_x = end_x
        self.y = y

    def __str__(self) -> str:
        return f"Number({self.value}, start_x: {self.start_x}, end_x: {self.end_x}, y: {self.y})"

    def __repr__(self) -> str:
        return f"Number({self.value}, start_x: {self.start_x}, end_x: {self.end_x}, y: {self.y})"


def get_numbers(board):
    numbers = []
    for i in range(len(board)):
        curr_number = ""
        number_start_index = -1
        for j in range(len(board[i])):
            if board[i][j].isdigit():
                curr_number += board[i][j]
                if number_start_index == -1:
                    number_start_index = j
            if curr_number and not board[i][j].isdigit():
                numbers.append(
                    Number(
                        int(curr_number),
                        number_start_index,
                        j - 1,
                        i,
                    )
                )
                curr_number = ""
                number_start_index = -1
    return numbers


def check_adjacent(board, number):
    for i in range(number.y - 1, number.y + 2):
        for j in range(number.start_x - 1, number.end_x + 2):
            if i == number.y and j == number.start_x:
                continue
            if i == number.y and j == number.end_x:
                continue
            if i < 0 or i >= len(board):
                continue
            if j < 0 or j >= len(board[i]) - 1:
                continue
            if not board[i][j].isdigit() and board[i][j] != ".":
                return True
    return False


def main():
    with open("../input") as f:
        lines = f.readlines()

    board = [list(line) for line in lines]

    numbers = get_numbers(board)
    numbers = list(filter(lambda number: check_adjacent(board, number), numbers))

    answer = sum(map(lambda number: number.value, numbers))
    print(answer)


if __name__ == "__main__":
    main()
