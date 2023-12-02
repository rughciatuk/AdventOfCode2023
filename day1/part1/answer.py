import re

if __name__ == "__main__":
    with open("../input", "r") as input_f:
        data = input_f.readlines()

    current_sum = 0
    # Filter all chacter that aren't digits
    for line in data:
        digits = "".join(re.findall(r"\d+", line))
        current_sum += int(digits[0]) * 10 + int(digits[-1])

    print(current_sum)
