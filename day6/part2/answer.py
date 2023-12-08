def parse(lines):
    times = int(lines[0].split(": ")[1].strip().replace(" ", ""))
    dist = int(lines[1].split(": ")[1].strip().replace(" ", ""))
    return times, dist


def calc_race(time, min_dist):
    winning = 0
    for i in range(time + 1):
        curr_dist = (time - i) * i
        if curr_dist > min_dist:
            winning += 1
    return winning


def main():
    with open("../input") as f:
        lines = f.readlines()
    data = parse(lines)

    total = calc_race(data[0], data[1])
    print(total)


if __name__ == "__main__":
    main()
