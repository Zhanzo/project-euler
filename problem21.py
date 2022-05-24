def get_divisor_sum(number: int) -> int:
    divisor_sum: int = 0
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            divisor_sum += i
    return divisor_sum


def solve(number: int) -> int:
    divisor_sums: list[int] = [get_divisor_sum(i) for i in range(number)]
    amicable_numbers_sum: int = 0

    for a in range(number):
        b = divisor_sums[a]
        if b <= number and b != a and a == divisor_sums[b]:
            amicable_numbers_sum += a

    return amicable_numbers_sum


if __name__ == "__main__":
    print(solve(10000))
