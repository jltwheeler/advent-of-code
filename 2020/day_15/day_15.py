def main(inputs: list, num: int) -> int:
    numbers = [int(num) for num in inputs[0].split(",")]

    spoken = {}
    last_num = 0
    for i in range(num):
        if i < len(numbers):
            spoken[numbers[i]] = [{"turn": i, "count": 1}]
            last_num = numbers[i]
            continue

        if len(spoken[last_num]) == 1:
            if 0 not in spoken:
                spoken[0] = [{"turn": i, "count": 1}]
            else:
                spoken[0] = [
                    spoken[0][-1],
                    {"turn": i, "count": spoken[0][-1]["count"] + 1},
                ]
            last_num = 0
        else:
            result = (
                spoken[last_num][-1]["turn"] - spoken[last_num][-2]["turn"]
            )
            if result not in spoken:
                spoken[result] = [{"turn": i, "count": 1}]
            else:
                spoken[result] = [
                    spoken[result][-1],
                    {"turn": i, "count": spoken[result][-1]["count"] + 1},
                ]

            last_num = result

    return last_num


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inputs = f.readlines()

    # print(main(inputs, 2020))
    print(main(inputs, 30000000))

