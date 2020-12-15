import re

regex_mask = re.compile(r"[0-1X]+.*$")
regex_add = re.compile(r"\[(\d+)\]")
regex_val = re.compile(r"\d*$")


def part_one(inputs: list) -> int:
    addresses = {}
    for input_ in inputs:
        mask = regex_mask.findall(input_[0])[0].zfill(36)
        mask_idxs = [i for i, x in enumerate(list(mask)) if x != "X"]

        for line in input_[1:]:
            address = regex_add.findall(line)[0]
            val = regex_val.findall(line)[0]

            val_bin = f"{int(val):b}".zfill(36)
            for idx in mask_idxs:
                val_bin = val_bin[:idx] + mask[idx] + val_bin[idx + 1 :]

            addresses[address] = int(val_bin, 2)

    return sum(addresses.values())


def part_two(inputs: list) -> int:
    addresses = {}
    for input_ in inputs:
        mask = regex_mask.findall(input_[0])[0].zfill(36)
        mask_idxs = [i for i, x in enumerate(list(mask)) if x != "0"]

        for line in input_[1:]:
            address = int(regex_add.findall(line)[0])
            decimal = int(regex_val.findall(line)[0])

            val_bin = f"{int(address):b}".zfill(36)
            for idx in mask_idxs:
                val_bin = val_bin[:idx] + mask[idx] + val_bin[idx + 1 :]

            floating_idxs = [i for i, x in enumerate(list(mask)) if x == "X"]

            for i in range(2 ** len(floating_idxs)):
                vals = list(f"{int(i):b}".zfill(len(floating_idxs)))

                for val, idx in zip(vals, floating_idxs):
                    val_bin = val_bin[:idx] + val + val_bin[idx + 1 :]
                addresses[int(val_bin, 2)] = decimal

    return sum(addresses.values())


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()

    inputs = []
    count = 0
    for line in lines:
        if "mask" in line:
            inputs.append([line])
            count += 1
        else:
            inputs[count - 1].append(line)

    print(part_one(inputs))
    print(part_two(inputs))

