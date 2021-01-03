import math


def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False

    for i in range(5, math.ceil(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True


def find_max_pow(number: int, end: int) -> int:
    power: int = 1
    while pow(number, power) <= end:
        power += 1
    return power - 1


def solve(end: int) -> int:
    product: int = 1
    for i in range(end):
        if is_prime(i):
            product *= pow(i, find_max_pow(i, end))
    return product


if __name__ == "__main__":
    print(solve(20))
