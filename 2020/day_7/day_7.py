import re


def part_one(inputs: list, bag_color: str) -> int:
    bag_colors = []

    def walk(inputs, bag_color, bag_colors):
        for line in inputs:
            split_text = line.split("contain")
            if bag_color in split_text[1]:
                parent_bag = split_text[0].split("bags")[0].strip()

                if parent_bag == bag_color:
                    return bag_colors

                if parent_bag not in bag_colors:
                    bag_colors.append(parent_bag)

                bag_colors = walk(inputs, parent_bag, bag_colors)
        return bag_colors

    bag_colors = walk(inputs, bag_color, bag_colors)
    return len(bag_colors)


def part_two(inputs: list, bag_color: str):
    bags = []
    regex = re.compile(r"\d")

    def walk(inputs, bag_color, bags):
        for i, line in enumerate(inputs):
            split_text = line.split("contain")
            if bag_color in split_text[0]:
                if "no other bag" in split_text[1]:
                    return bags
                for child in split_text[1].split(","):
                    text = child.split("bag")[0].strip()
                    count = int(regex.findall(text)[0])
                    bag_color = str(regex.sub("", text))

                    for _ in range(count):
                        bags.extend([bag_color])
                        bags = walk(inputs, bag_color.strip(), bags)
        return bags

    bags = walk(inputs, bag_color, bags)

    return len(bags)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inputs = f.read().split("\n")

    print(part_one(inputs, "shiny gold"))
    print(part_two(inputs, "shiny gold"))
