def solve(maximum: int) -> int:
    lower: int = 0
    upper: int = 1
    sum_even: int = 0
    while upper < maximum:
        sum_lower_upper: int = lower + upper
        lower = upper
        upper = sum_lower_upper
        if upper % 2 == 0:
            sum_even += upper
    return sum_even


if __name__ == "__main__":
    print(solve(4000000))
