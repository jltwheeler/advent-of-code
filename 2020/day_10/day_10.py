def part_one(inputs: list) -> int:
    sorted_inputs = sorted(inputs)

    three_jolts = 0
    one_jolts = 0

    for i, x in enumerate(sorted_inputs):
        diff = x - sorted_inputs[i - 1] if i > 0 else x
        if diff == 1:
            one_jolts += 1
        elif diff == 3:
            three_jolts += 1

    three_jolts += 1

    return three_jolts * one_jolts


def part_two(inputs: list) -> int:
    sorted_inputs = sorted(inputs)
    sorted_inputs.append(max(sorted_inputs) + 3)
    sorted_inputs.insert(0, 0)
    num_arrangements = 0

    mem = {}

    def walk(i, sorted_inputs):
        if i in mem:
            return mem[i]

        if i == len(sorted_inputs) - 1:
            return 1
        count = 0
        for j in range(i + 1, len(sorted_inputs)):
            if sorted_inputs[j] - sorted_inputs[i] <= 3:
                count += walk(j, sorted_inputs)
        mem[i] = count
        return count

    num_arrangements += walk(0, sorted_inputs)

    return num_arrangements


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.read().split("\n")

    inputs = [int(line) for line in lines]

    print(part_one(inputs))
    print(part_two(inputs))

