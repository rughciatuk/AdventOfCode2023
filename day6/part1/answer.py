def parse(lines):
    times = [int(x) for x in lines[0].split(": ")[1].strip().split(" ") if x]
    dist = [int(x) for x in lines[1].split(": ")[1].strip().split(" ") if x]

    return list(zip(times, dist))


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

    total = 1
    for time, min_dist in data:
        total *= calc_race(time, min_dist)

    print(total)


if __name__ == "__main__":
    main()
