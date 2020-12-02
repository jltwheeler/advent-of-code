def part_one(expenses: list) -> int:
    for i, expense in enumerate(expenses):
        if (2020 - expense) in expenses:
            return expense * (2020 - expense)


def part_two(expenses: list) -> int:
    for i, expense in enumerate(expenses):
        for j in range(len(expenses)):
            if i != j and (2020 - expense - expenses[j]) in expenses:
                return expense * expenses[j] * (2020 - expense - expenses[j])


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inputs = f.readlines()

    data = [int(input_) for input_ in inputs]

    print(part_one(data))
    print(part_two(data))
