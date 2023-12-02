import re

rules = {"red": 12, "green": 13, "blue": 14}


def check_game(game):
    for sub_game in game.split("; "):
        for cube_subset in sub_game.split(", "):
            split_cube = cube_subset.split(" ")
            number_of_cube = int(split_cube[0])
            cube_type = split_cube[1]
            if rules[cube_type] < number_of_cube:
                return False
    return True


def main():
    with open("../input", "r") as f:
        input = f.readlines()

        sum = 0
    for line in input:
        game_id = re.search(r"^Game (\d+)", line).groups()[0]
        # Remove the game bit
        line = line.split(":", 1)[1].strip()
        if check_game(line):
            sum += int(game_id)
    print(sum)


if __name__ == "__main__":
    main()
