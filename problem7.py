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


def solve(max_primes: int) -> int:
    primes: list[int] = []
    number: int = 1
    while len(primes) < max_primes:
        if is_prime(number):
            primes.append(number)
        number += 1
    return primes[-1]


if __name__ == "__main__":
    print(solve(10001))
