def part_one(inputs: list) -> int:
    timestamp = int(inputs[0])
    buses = [int(bus) for bus in inputs[1].split(",") if bus != "x"]

    earliest_departs = {}
    for bus in buses:
        init_time = 0
        counter = 0
        while init_time < timestamp:
            init_time = bus * counter
            counter += 1
        earliest_departs[bus] = init_time

    earliest = min(earliest_departs.values())
    idx = list(earliest_departs.values()).index(earliest)
    bus_id = list(earliest_departs.keys())[idx]
    wait = earliest - timestamp
    return wait * bus_id


def part_two(inputs: list) -> int:
    bus_times = {}
    for i, bus in enumerate(inputs[1].split(",")):
        if bus != "x":
            bus_times[int(bus)] = -i % int(bus) if i > 0 else 0

    bus_ids_asc = sorted(bus_times)[::-1]
    rem = bus_ids_asc[0]
    val = bus_times[rem]
    for x in bus_ids_asc[1:]:
        while val % x != bus_times[x]:
            val += rem
        rem *= x
    return val


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inputs = f.readlines()


    print(part_one(inputs))
    print(part_two(inputs))

