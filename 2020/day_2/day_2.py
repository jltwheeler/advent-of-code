def get_important_values(input_: str) -> tuple:
    occ, letter, password = input_.split(" ")

    letter = letter[:-1]
    password_list = list(password)
    num_1 = int(occ.split("-")[0])
    num_2 = int(occ.split("-")[-1])

    return letter, password_list, num_1, num_2



def part_one(inputs: list) -> int:
    num_valid = 0
    for input_ in inputs:
        letter, password_list, min_occ, max_occ = get_important_values(input_)
        if (
            password_list.count(letter) <= max_occ  and
            password_list.count(letter) >= min_occ
        ):
            num_valid += 1

    return num_valid


def part_two(inputs: list) -> int:
    num_valid = 0
    for input_ in inputs:
        valid = False
        letter, password_list, idx_1, idx_2 = get_important_values(input_)

        for idx, item in enumerate(password_list, 1):
            if item == letter and idx == idx_1:
                valid = True
            if item == letter and idx == idx_2:
                valid = not valid
        if valid:
            num_valid += 1

    return num_valid

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inputs = f.readlines()

    test_inputs = [
        "1-3 a: abcde",
        "1-3 b: cdefg",
        "2-9 c: ccccccccc"
    ]

    print(part_one(inputs))
    print(part_two(inputs))