import math


def solve(number: int) -> int:
    return get_digit_sum(math.factorial(number))


def get_digit_sum(number: int) -> int:
    return sum(int(digit) for digit in str(number))


if __name__ == "__main__":
    print(solve(100))