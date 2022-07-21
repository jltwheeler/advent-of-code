def part_one(inputs: list, pre_len: int) -> int:
    for i, num in enumerate(inputs):
        if i > pre_len - 1:
            preamble = inputs[i - pre_len : i]

            exists = any(num - item in preamble for item in preamble)
            if not exists:
                return num
    return 0


def part_two(inputs: list, invalid_num: int) -> int:
    for i, num in enumerate(inputs):
        nums = [num]
        j = i + 1
        while sum(nums) < invalid_num:
            nums.append(inputs[j])
            j += 1

            if sum(nums) == invalid_num:
                return max(nums) + min(nums)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.read().split("\n")

    inputs = [int(line) for line in lines]

    invalid_num = part_one(inputs, 25)
    print(invalid_num)
    print(part_two(inputs, invalid_num))
