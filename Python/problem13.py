def read_file() -> list[int]:
    with open("problem13.txt", "r") as fp:
        return [int(line) for line in fp.readlines()]


def solve(numbers: list[int]) -> int:
    sigma: int = sum(numbers)
    return int(str(sigma)[:10])


if __name__ == "__main__":
    numbers: list[int] = read_file()
    print(solve(numbers))
