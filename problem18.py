def read_input() -> list[list[int]]:
    with open("problem18.txt", "r") as fp:
        return [[int(i) for i in line.strip().split(" ")] for line in fp.readlines()]


def solve(pyramid: list[list[int]], row: int, col: int) -> int:
    if row >= len(pyramid) or col >= len(pyramid[row]):
        return 0
    return pyramid[row][col] + max(
        solve(pyramid, row + 1, col), solve(pyramid, row + 1, col + 1)
    )


if __name__ == "__main__":
    pyramid: list[list[int]] = read_input()
    print(solve(pyramid, 0, 0))
