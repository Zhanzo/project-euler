def get_divisor_sum(number: int) -> int:
    divisor_sum: int = 0

    for i in range(1, number // 2 + 1):
        if number % i == 0:
            divisor_sum += i

    return divisor_sum


def get_abundant_numbers(limit: int) -> list[int]:
    return list(filter(lambda a: get_divisor_sum(a) > a, [i for i in range(limit)]))


def get_abundant_sums(abundant_numbers: list[int], limit: int) -> list[int]:
    abundant_sums: list[int] = []

    for a in abundant_numbers:
        for b in abundant_numbers:
            if a + b < limit:
                abundant_sums.append(a + b)

    return abundant_sums


def solve(limit: int) -> int:
    abundant_numbers: list[int] = get_abundant_numbers(limit)
    abundant_sums: list[int] = get_abundant_sums(abundant_numbers, limit)
    non_abundant_sum: int = 0

    for num in range(1, limit):
        if num not in abundant_sums:
            non_abundant_sum += num

    return non_abundant_sum


if __name__ == "__main__":
    print(solve(28124))
