import math


def find_num_divisors(num: int) -> int:
    count: int = 0
    for i in range(1, math.ceil(math.sqrt(num))):
        if num % i == 0:
            count += 2
    return count


def solve() -> int:
    num: int = 0
    i: int = 1
    while True:
        num += i
        i += 1
        if find_num_divisors(num) >= 500:
            return num


if __name__ == "__main__":
    print(solve())
