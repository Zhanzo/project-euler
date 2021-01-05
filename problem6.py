def calc_square_sum(number: int) -> int:
    return pow(sum([i for i in range(1, number + 1)]), 2)


def calc_sum_squares(number: int) -> int:
    return sum([pow(i, 2) for i in range(1, number + 1)])


def solve(number: int) -> int:
    square_sum: int = calc_square_sum(number)
    sum_squares: int = calc_sum_squares(number)
    return square_sum - sum_squares


if __name__ == "__main__":
    print(solve(100))
