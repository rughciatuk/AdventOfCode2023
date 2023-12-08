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


def main():
    with open("../input") as f:
        data = parse(f.read())

    locations = []
    for seed in data.seeds:
        curr_value = seed
        curr_value = get_next(data.seed_to_soil, curr_value)
        curr_value = get_next(data.soil_to_fertilizer, curr_value)
        curr_value = get_next(data.fertilizer_to_water, curr_value)
        curr_value = get_next(data.water_to_light, curr_value)
        curr_value = get_next(data.light_to_temperature, curr_value)
        curr_value = get_next(data.temperature__to_humidity, curr_value)
        curr_value = get_next(data.humidity_to_location, curr_value)
        locations.append(curr_value)
    print(min(locations))


if __name__ == "__main__":
    main()
