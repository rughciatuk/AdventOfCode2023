from collections import Counter

ALPHABET = "J23456789TQKA"[::-1]


def parse(lines):
    data = []
    for line in lines:
        hand, bid = line.split(" ")
        bid = int(bid.strip())
        data.append((hand, bid))
    return data


def get_first_order(hand):
    joker_count = hand.count("J")
    # removing jokers
    hand = hand.replace("J", "")

    counter = Counter(hand)
    occ_values = list(counter.values())
    print(occ_values)

    if joker_count == 5:
        return 6

    occ_values[occ_values.index(max(occ_values))] += joker_count

    if 5 in occ_values:
        return 6
    elif 4 in occ_values:
        return 5
    elif set(occ_values) == set([2, 3]):
        return 4
    elif 3 in occ_values:
        return 3
    elif occ_values.count(2) == 2:
        return 2
    elif 2 in occ_values:
        return 1
    else:
        return 0


def get_second_order(data):
    # sorting by first order
    buckets = [[] for _ in range(7)]
    for hand, bid, first_order in data:
        buckets[first_order].append((hand, bid))
    # sorting by second order
    for bucket in buckets:
        bucket.sort(key=lambda x: [ALPHABET.index(c) for c in x[0]], reverse=True)

    # joining the buckets together
    data = []
    for bucket in buckets:
        data.extend(bucket)

    return data


def main():
    with open("../input") as f:
        lines = f.readlines()

    data = parse(lines)
    for index, (hand, bid) in enumerate(data):
        data[index] = (hand, bid, get_first_order(hand))

    data.sort(key=lambda x: x[2])
    data = get_second_order(data)

    total = 0
    for index, (hand, bid) in enumerate(data):
        total += bid * (index + 1)
    print(total)


if __name__ == "__main__":
    main()
