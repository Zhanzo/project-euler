def get_divisor_sum(number: int) -> int:
    divisor_sum: int = 0
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            divisor_sum += i
    return divisor_sum


def solve(number: int) -> int:
    divisor_sums: list[int] = [0 for _ in range(number)]
    for i in range(1, number):
        divisor_sums[i] = get_divisor_sum(i)

    amicable_numbers_sum: int = 0
    for i in range(1, number):
        if (
            divisor_sums[i] <= number
            and i != divisor_sums[i]
            and i == divisor_sums[divisor_sums[i]]
        ):
            amicable_numbers_sum += i
    return amicable_numbers_sum


if __name__ == "__main__":
    print(solve(10000))
