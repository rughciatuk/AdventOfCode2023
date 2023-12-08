from math import lcm


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

    # Finding all of locations that end with A
    curr_locations = list(filter(lambda x: x[2] == "A", locations.keys()))

    finish_values = dict()
    index = 0
    while True:
        number_of_finish = 0
        for curr_location_index, curr_location in enumerate(curr_locations):
            curr_locations[curr_location_index] = locations[curr_location][
                walk_seq[index % len(walk_seq)]
            ]
            if curr_locations[curr_location_index][2] == "Z":
                if curr_location_index not in finish_values:
                    finish_values[curr_location_index] = index + 1
                # done with this one
        if number_of_finish == len(curr_locations):
            break
        if len(finish_values.keys()) == len(curr_locations):
            break
        index += 1

    print(lcm(*finish_values.values()))


# while True:
#     curr_location = locations[curr_location][walk_seq[index % len(walk_seq)]]
#     if curr_location == "ZZZ":
#         break
#     index += 1

# print(index + 1)


if __name__ == "__main__":
    main()
