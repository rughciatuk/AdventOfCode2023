import re


def check_game(game):
    current_power_set = {"red": 0, "green": 0, "blue": 0}
    for sub_game in game.split("; "):
        for cube_subset in sub_game.split(", "):
            split_cube = cube_subset.split(" ")
            number_of_cube = int(split_cube[0])
            cube_type = split_cube[1]
            current_power_set[cube_type] = max(
                number_of_cube, current_power_set[cube_type]
            )

    return (
        current_power_set["red"]
        * current_power_set["green"]
        * current_power_set["blue"]
    )


def main():
    with open("../input", "r") as f:
        input = f.readlines()

        sum = 0
    for line in input:
        game_id = re.search(r"^Game (\d+)", line).groups()[0]
        # Remove the game bit
        line = line.split(":", 1)[1].strip()
        sum += check_game(line)
    print(sum)


if __name__ == "__main__":
    main()
