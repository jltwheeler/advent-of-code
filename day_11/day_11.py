def part_one(inputs: list) -> int:
    prev = ""
    new = "\n".join("".join(line) for line in inputs)

    while prev != new:
        prev = new
        new_seats = []

        for i, line in enumerate(inputs):
            new_row = []
            for j in range(len(line)):
                if line[j] == ".":
                    new_row.append(".")
                    continue

                count = 0
                for dx, dy in [
                    (0, 1),
                    (1, 0),
                    (-1, 0),
                    (0, -1),
                    (1, 1),
                    (1, -1),
                    (-1, 1),
                    (-1, -1),
                ]:
                    if i + dy >= 0 and j + dx >= 0:
                        try:
                            if inputs[i + dy][j + dx] == "#":
                                count += 1
                        except IndexError:
                            pass

                if count >= 4:
                    new_row.append("L")
                elif count == 0:
                    new_row.append("#")
                else:
                    new_row.append(inputs[i][j])
            new_seats.append(new_row)
        inputs = new_seats

        new = "\n".join("".join(line) for line in inputs)

    return new.count("#")


def part_two(inputs: list) -> int:
    prev = ""
    new = "\n".join("".join(line) for line in inputs)

    while prev != new:
        prev = new
        new_seats = []

        for i, line in enumerate(inputs):
            new_row = []
            for j in range(len(line)):
                if line[j] == ".":
                    new_row.append(".")
                    continue

                count = 0
                dist_left = j - 0
                dist_right = len(line) - 1 - j
                dist_up = i - 0
                dist_down = len(inputs) - 1 - i
                for dir in [
                    [(0, 1)] * dist_down,
                    [(1, 0)] * dist_right,
                    [(-1, 0)] * dist_left,
                    [(0, -1)] * dist_up,
                    [(1, 1)] * min(dist_right, dist_down),
                    [(1, -1)] * min(dist_right, dist_up),
                    [(-1, 1)] * min(dist_left, dist_down),
                    [(-1, -1)] * min(dist_left, dist_up),
                ]:
                    for m, (dx, dy) in enumerate(dir, 1):
                        if i + dy * m >= 0 and j + dx * m >= 0:
                            try:
                                if inputs[i + dy * m][j + dx * m] == "#":
                                    count += 1
                                    break
                                elif inputs[i + dy * m][j + dx * m] == "L":
                                    break
                            except IndexError:
                                pass

                if count >= 5:
                    new_row.append("L")
                elif count == 0:
                    new_row.append("#")
                else:
                    new_row.append(inputs[i][j])
            new_seats.append(new_row)
        inputs = new_seats

        new = "\n".join("".join(line) for line in inputs)

    return new.count("#")


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.read().split("\n")

    inputs = [list(line) for line in lines]

    print(part_one(inputs))
    print(part_two(inputs))

