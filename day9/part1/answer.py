def parse(lines):
    data = [[int(x) for x in line.strip().split(" ")] for line in lines]

    return data


def predicate(history):
    # We need to calculate the diffrences between every 2 number and add it to a new array
    diffs = []
    only_0 = len(set(history)) == 1 and history[0] == 0
    diffs.append(history)
    curr_diff_index = 1
    while not only_0:
        diffs.append([])
        for i in range(len(diffs[curr_diff_index - 1]) - 1):
            diffs[curr_diff_index].append(
                diffs[curr_diff_index - 1][i + 1] - diffs[curr_diff_index - 1][i]
            )

        only_0 = (
            len(set(diffs[curr_diff_index])) == 1 and diffs[curr_diff_index][0] == 0
        )
        curr_diff_index += 1

    # back to front
    diffs.reverse()
    for index, diff in enumerate(diffs):
        if index == 0:
            continue
        diff.append(diff[-1] + diffs[index - 1][-1])

    return diffs[-1][-1]


def main():
    with open("../input") as f:
        lines = f.readlines()
    data = parse(lines)

    total = 0
    for line in data:
        total += predicate(line)

    print(total)


if __name__ == "__main__":
    main()
