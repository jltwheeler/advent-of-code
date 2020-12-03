def build_grid(lines: list) -> list:
    grid = []
    for line in lines:
        layout = [cell for cell in list(line) if cell in [".", "#"]]
        grid.append(layout)
    return grid

def count_trees(grid: list, right: int, down: int) -> int:
    pos = 0
    tree_count = 0

    for i in range(0, len(grid), down):
        line = grid[i]
        if line[pos] == "#":
            tree_count += 1

        pos += right
        if pos > len(line) - 1:
            pos -= len(line)

    return tree_count


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inputs = f.readlines()

    grid = build_grid(inputs)

    # Part one
    print(count_trees(grid, 3, 1))

    # Part two
    print(
        count_trees(grid, 1, 1) *
        count_trees(grid, 3, 1) *
        count_trees(grid, 5, 1) *
        count_trees(grid, 7, 1) *
        count_trees(grid, 1, 2)
    )
