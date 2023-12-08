def parse(lines):
    walk_seq = [0 if x == "L" else 1 for x in lines[0].strip()]

    locations = dict()
    for line in lines[2:]:
        location, targets_str = line.strip().split(" = ")
        targets_str = targets_str.replace("(", "")
        targets_str = targets_str.replace(")", "")
        locations[location] = tuple(targets_str.split(", "))

    return walk_seq, locations


def main():
    with open("../input") as f:
        lines = f.readlines()
    walk_seq, locations = parse(lines)

    index = 0
    curr_location = "AAA"

    while True:
        curr_location = locations[curr_location][walk_seq[index % len(walk_seq)]]
        if curr_location == "ZZZ":
            break
        index += 1

    print(index + 1)


if __name__ == "__main__":
    main()
