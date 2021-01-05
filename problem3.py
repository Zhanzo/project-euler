import math


def is_prime(number: int) -> bool:
    for i in range(2, math.ceil(math.sqrt(number)), 1):
        if number % i == 0:
            return False
    return True


def solve(number: int) -> int:
    factor: int = 0
    for i in range(1, math.ceil(math.sqrt(number)), 1):
        if number % i == 0:
            if is_prime(i):
                factor = i
    return factor


if __name__ == "__main__":
    print(solve(600851475143))
