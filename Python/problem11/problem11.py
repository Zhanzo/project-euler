def read_input() -> list[list[int]]:
    with open("data.txt", "r") as fp:
        return [string_to_int(line.split(" ")) for line in fp.readlines()]


def string_to_int(line: list[str]) -> list[int]:
    return [int(num) for num in line]


def down_product(grid: list[list[int]], row_index: int,
                 column_index: int) -> int:
    if row_index + 4 >= len(grid):
        return 0
    product: int = 1
    for i in range(4):
        product *= grid[row_index + i][column_index]
    return product


def right_product(grid: list[list[int]], row_index: int,
                  column_index: int) -> int:
    if column_index + 4 >= len(grid[0]):
        return 0
    product: int = 1
    for i in range(4):
        product *= grid[row_index][column_index + i]
    return product


def diag_left_product(grid: list[list[int]], row_index: int,
                      column_index: int) -> int:
    if row_index + 4 >= len(grid) or column_index - 4 < 0:
        return 0
    product: int = 1
    for i in range(4):
        product *= grid[row_index + i][column_index - i]
    return product


def diag_right_product(grid: list[list[int]], row_index: int,
                       column_index: int) -> int:
    if row_index + 4 >= len(grid) or column_index + 4 >= len(grid[0]):
        return 0
    product: int = 1
    for i in range(4):
        product *= grid[row_index + i][column_index + i]
    return product


def solve(grid: list[list[int]]):
    greatest_product: int = 0
    for row_index in range(len(grid)):
        for column_index in range(len(grid[row_index])):
            local_greatest_product: int = max(
                down_product(grid, row_index, column_index),
                right_product(grid, row_index, column_index),
                diag_left_product(grid, row_index, column_index),
                diag_right_product(grid, row_index, column_index)
                )
            if local_greatest_product > greatest_product:
                greatest_product = local_greatest_product
    return greatest_product


grid = read_input()
print(grid)
print(solve(grid))
