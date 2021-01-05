def solve(size: int):
    grid: list[list[int]] = [[1 for _ in range(size + 1)] for _ in range(size + 1)]
    for i in range(size):
        for j in range(size):
            grid[i + 1][j] += grid[i][j]
            grid[i][j + 1] += grid[i][j]
    return grid[size][size - 1]


if __name__ == "__main__":
    print(solve(20))
