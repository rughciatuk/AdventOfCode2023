PIPE_OPTIONS = "|-LJ7F"


class Map:
    def __init__(self, board, starting_point):
        self.board = board
        self.starting_point = starting_point

    def get(self, point):
        return self.board[point[1]][point[0]]

    def test(self, points):
        for point in points:
            if point[0] < 0 or point[1] < 0:
                return False
            elif point[0] >= len(self.board[0]) or point[1] >= len(self.board):
                return False

        return points

    def get_next_points(self, point):
        # print(self.board)
        # print(f"Getting next points for {point}, which is {self.get(point)}")
        match self.get(point):
            case "|":
                return self.test([(point[0], point[1] + 1), (point[0], point[1] - 1)])
            case "-":
                return self.test([(point[0] + 1, point[1]), (point[0] - 1, point[1])])
            case "L":
                return self.test([(point[0], point[1] - 1), (point[0] + 1, point[1])])
            case "J":
                return self.test([(point[0], point[1] - 1), (point[0] - 1, point[1])])
            case "7":
                return self.test([(point[0], point[1] + 1), (point[0] - 1, point[1])])
            case "F":
                return self.test([(point[0], point[1] + 1), (point[0] + 1, point[1])])
            case _:
                return False

    def __repr__(self):
        return f"Map(board={self.board}, starting_point={self.starting_point})"


def find_path(map):
    # loop over the map until we get back to the start
    # check both way
    total_distance = []
    for i in range(2):
        current_distance = 0
        curr_point = map.starting_point
        maybe_next = map.get_next_points(curr_point)

        if not maybe_next:
            return False
        next_point = maybe_next[i]
        while next_point and next_point != map.starting_point:
            current_distance += 1
            prev_point = curr_point
            curr_point = next_point
            maybe_next = map.get_next_points(curr_point)
            if not maybe_next:
                return False
            next_point = (
                maybe_next[i] if maybe_next[i] != prev_point else maybe_next[1 - i]
            )

        total_distance.append(current_distance)

    return total_distance


def find_max_distance(map):
    # First we need to find the right pipe to replace the starting point with
    for new_pipe in PIPE_OPTIONS:
        map.board[map.starting_point[1]][map.starting_point[0]] = new_pipe
        distance = find_path(map)
        if distance:
            return distance[0] // 2 + 1


def parse(lines):
    board = []
    for line in lines:
        board.append(list(line.strip()))

    # Find starting point
    starting_point = None
    for i, x in enumerate(board):
        if "S" in x:
            starting_point = (x.index("S"), i)
            break

    return Map(board, starting_point)


def main():
    with open("../input") as f:
        lines = f.readlines()

    map = parse(lines)
    print(find_max_distance(map))


if __name__ == "__main__":
    main()
