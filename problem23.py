import math


def get_divisors(number: int) -> set[int]:
    divisors: set = set([1])
    for i in range(2, math.ceil(math.sqrt(number)) + 1):
        if number % i == 0 and i < number:
            divisors.add(i)
            divisors.add(number // i)
    return divisors


def get_divisor_sum(number: int) -> int:
    return sum(get_divisors(number))


def get_abundant_numbers(number: int) -> list[int]:
    return list(filter(lambda a: get_divisor_sum(a) > a, [i for i in range(number)]))


def solve(number: int) -> int:
    abundant_numbers: list[int] = get_abundant_numbers(number)
    non_abundant_nums: list[int] = [i for i in range(number)]
    for i in range(len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            number_sum: int = abundant_numbers[i] + abundant_numbers[j]
            if number_sum < number:
                non_abundant_nums[number_sum] = 0
            else:
                break
    return sum(non_abundant_nums)


if __name__ == "__main__":
    print(solve(28124))
