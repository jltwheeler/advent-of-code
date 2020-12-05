import math


def get_boarding_id(boarding: str) -> int:
    row_upper = 127
    row_lower = 0
    col_upper = 7
    col_lower = 0

    for char in list(boarding):
        if char == "F":
            row_upper -= (row_upper - row_lower) / 2
            row_upper = math.floor(row_upper)
        elif char == "B":
            row_lower += (row_upper - row_lower) / 2
            row_lower = math.ceil(row_lower)
        elif char == "L":
            col_upper -= (col_upper - col_lower) / 2
            col_upper = math.floor(col_upper)
        else:
            col_lower += (col_upper - col_lower) / 2
            col_lower = math.ceil(col_lower)

    row = row_lower if boarding[6] == "F" else row_upper
    col = col_lower if boarding[-1] == "L" else col_upper

    return row * 8 + col


def find_missing_id(min_id: int, max_id: int) -> int:
    for x in range(min_id, max_id + 1, 1):
        if x not in ids:
            return x
    return False


def part_one(boarding: str) -> int:
    ids = [get_boarding_id(boarding) for boarding in boardings]

    return ids


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        boardings = f.read().split("\n")

    ids = part_one(boardings)
    min_id = min(ids)
    max_id = max(ids)

    print(max_id)
    print(find_missing_id(min_id, max_id))
