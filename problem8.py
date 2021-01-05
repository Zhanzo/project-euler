import functools


def read_file() -> list[int]:
    with open("problem8.txt", "r") as fp:
        contents: str = fp.read().replace("\n", "")
        return [int(i) for i in contents]


def calc_product(number: list[int], index: int, adjacent_numbers: int):
    return functools.reduce(
        lambda a, b: a * b,
        [number[index + offset] for offset in range(adjacent_numbers)],
    )


def solve(number: list[int], adjacent_numbers: int) -> int:
    max_prod = 0
    for i in range(len(number) - adjacent_numbers - 1):
        prod: int = calc_product(number, i, adjacent_numbers)
        if prod > max_prod:
            max_prod = prod
    return max_prod


if __name__ == "__main__":
    number: list[int] = read_file()
    print(solve(number, 13))
