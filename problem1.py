def solve(maximum: int) -> int:
    sum_divisible: int = 0
    for i in range(3, maximum):
        if i % 3 == 0 or i % 5 == 0:
            sum_divisible += i
    return sum_divisible


if __name__ == "__main__":
    print(solve(1000))
