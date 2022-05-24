def solve(number: int) -> int:
    for a in range(1, number):
        for b in range(a + 1, number):
            c: int = number - a - b
            if is_pythagorean(a, b, c):
                return a * b * c
    return 0


def is_pythagorean(a: int, b: int, c: int) -> bool:
    return pow(a, 2) + pow(b, 2) == pow(c, 2)


if __name__ == "__main__":
    print(solve(1000))
