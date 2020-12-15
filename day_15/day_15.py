def main(inputs: list, num: int) -> int:
    numbers = [int(num) for num in inputs[0].split(",")]

    results = []
    spoken = {}
    for i in range(num):
        if i < len(numbers):
            results.append(numbers[i])
            spoken[numbers[i]] = [{"turn": i, "count": 1}]
            continue

        last_num = results[-1]
        if len(spoken[last_num]) == 1:
            results.append(0)
            if 0 not in spoken:
                spoken[0] = [{"turn": i, "count": 1}]
            else:
                spoken[0].append(
                    {"turn": i, "count": spoken[0][-1]["count"] + 1}
                )
        else:
            result = (
                spoken[last_num][-1]["turn"] - spoken[last_num][-2]["turn"]
            )
            results.append(result)
            if result not in spoken:
                spoken[result] = [{"turn": i, "count": 1}]
            else:
                spoken[result].append(
                    {"turn": i, "count": spoken[result][-1]["count"] + 1}
                )

    return results[-1]


def part_two(inputs: list) -> int:
    pass


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inputs = f.readlines()

    print(main(inputs, 2020))
    print(main(inputs, 30000000))

