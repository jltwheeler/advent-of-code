def part_one(inputs: list):
    accumulator = 0
    line_num = 0
    line_nums = {}
    run = True

    while run:
        if line_num == len(inputs):
            return accumulator, line_nums, run

        input_ = inputs[line_num]
        verb = input_[:3]
        amount = int(input_.split(" ")[1])
        line_nums[line_num] = input_

        if verb == "nop":
            line_num += 1
        if verb == "jmp":
            line_num += amount
        if verb == "acc":
            accumulator += amount
            line_num += 1

        if line_num in line_nums:
            run = False

    return accumulator, line_nums, run


def part_two(inputs: list, line_nums: dict):
    lines = {}
    for key in line_nums:
        if "jmp" in line_nums[key] or "nop" in line_nums[key]:
            lines[key] = line_nums[key]

    for line, value in lines.items():
        new_inputs = inputs.copy()
        if "jmp" in value:
            new_inputs[line] = value.replace("jmp", "nop")
        else:
            new_inputs[line] = value.replace("nop", "jmp")

        acc, _, run = part_one(new_inputs)
        if run:
            return acc

    return None


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inputs = f.read().split("\n")

    accum, line_nums, run = part_one(inputs)
    print(accum)

    print(part_two(inputs, line_nums))
