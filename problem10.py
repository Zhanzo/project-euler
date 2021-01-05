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


def solve(max_number: int) -> int:
    prime_sum = 2
    for number in range(3, max_number, 2):
        if is_prime(number):
            prime_sum += number
    return prime_sum


if __name__ == "__main__":
    print(solve(2000000))
