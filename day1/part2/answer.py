import re

number_text_to_number = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

if __name__ == "__main__":
    with open("../input", "r") as input_f:
        data = input_f.readlines()

    current_sum = 0
    # Filter all chacter that aren't digits
    for line in data:
        order = re.findall(r"(one|two|three|four|five|six|seven|eight|nine)", line)

        for number in order:
            line = re.sub(number, number_text_to_number[number], line)
        digits = "".join(re.findall(r"\d+", line))
        current_sum += int(digits[0]) * 10 + int(digits[-1])

    print(current_sum)
