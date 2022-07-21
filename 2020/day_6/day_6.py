def clean_inputs(inputs: list) -> list:
    return [input_.replace("\n", "") for input_ in inputs]


def part_one(inputs: list) -> int:
    cleaned = clean_inputs(inputs)
    return sum(len(set(item)) for item in cleaned)


def part_two(inputs: list) -> int:
    count = 0
    for input_ in inputs:
        group = input_.split("\n")
        if len(group) == 1:
            count += len(group[0])
        else:
            chars = list(group[0])
            for char in chars:
                all = not any(char not in item for item in group[1:])
                if all:
                    count += 1

    return count


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inputs = f.read().split("\n\n")

    print(part_one(inputs))
    print(part_two(inputs))
