def solve(power: int) -> int:
    number: int = pow(2, power)
    return sum([int(i) for i in str(number)])


if __name__ == "__main__":
    print(solve(1000))
