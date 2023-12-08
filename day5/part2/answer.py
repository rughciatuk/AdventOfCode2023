class Data:
    def __init__(
        self,
        seeds,
        seed_to_soil,
        soil_to_fertilizer,
        fertilizer_to_water,
        water_to_light,
        light_to_temperature,
        temperature__to_humidity,
        humidity_to_location,
    ):
        self.seeds = seeds
        self.seed_to_soil = seed_to_soil
        self.soil_to_fertilizer = soil_to_fertilizer
        self.fertilizer_to_water = fertilizer_to_water
        self.water_to_light = water_to_light
        self.light_to_temperature = light_to_temperature
        self.temperature__to_humidity = temperature__to_humidity
        self.humidity_to_location = humidity_to_location

    @staticmethod
    def get_map(part):
        return [[int(j) for j in x.split(" ") if j] for x in part.split("\n")[1:] if x]


def parse(lines):
    # split on new lines on empty lines
    split_lines = lines.split("\n\n")
    # Getting the seeds data:
    seeds = [int(x) for x in split_lines[0].split(": ")[1].split(" ")]
    seeds = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]
    # Getting the seed to soil data:
    seed_to_soil = Data.get_map(split_lines[1])
    soil_to_fertilizer = Data.get_map(split_lines[2])
    fertilizer_to_water = Data.get_map(split_lines[3])
    water_to_light = Data.get_map(split_lines[4])
    light_to_temperature = Data.get_map(split_lines[5])
    temperature__to_humidity = Data.get_map(split_lines[6])
    humidity_to_location = Data.get_map(split_lines[7])
    return Data(
        seeds,
        seed_to_soil,
        soil_to_fertilizer,
        fertilizer_to_water,
        water_to_light,
        light_to_temperature,
        temperature__to_humidity,
        humidity_to_location,
    )


def get_next(curr_map, curr_value):
    for dest_start, source_start, length in curr_map:
        if curr_value in range(source_start, source_start + length + 1):
            return dest_start + curr_value - source_start
    return curr_value


def get_prev(curr_map, curr_value):
    for dest_start, source_start, length in curr_map:
        if curr_value - dest_start >= 0 and (curr_value - dest_start) < length:
            return source_start + curr_value - dest_start
        # if curr_value in range(dest_start, dest_start + length + 1):
        #     return source_start + curr_value - dest_start
    return curr_value


def check_if_in_seeds(seeds, curr_value):
    for start, length in seeds:
        if curr_value - start >= 0 and (curr_value - start) < length:
            return True
    return False


def main():
    with open("../input") as f:
        data = parse(f.read())

    location_start = 1
    # Reverse search
    while True:
        if location_start % 10000 == 0:
            print(location_start)
        curr_value = location_start
        curr_value = get_prev(data.humidity_to_location, curr_value)
        curr_value = get_prev(data.temperature__to_humidity, curr_value)
        curr_value = get_prev(data.light_to_temperature, curr_value)
        curr_value = get_prev(data.water_to_light, curr_value)
        curr_value = get_prev(data.fertilizer_to_water, curr_value)
        curr_value = get_prev(data.soil_to_fertilizer, curr_value)
        curr_value = get_prev(data.seed_to_soil, curr_value)
        if check_if_in_seeds(data.seeds, curr_value):
            print(location_start)
            break
        location_start += 1


if __name__ == "__main__":
    main()
