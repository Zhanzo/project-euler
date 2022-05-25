import math


def solve(permutation_value: int, values: list[int]) -> str:
    if len(values) == 1:
        return str(values[0])

    permutation: int = math.factorial(len(values) - 1)

    for i in range(len(values)):
        if (i + 1) * permutation > permutation_value:
            break

    value: int = values.pop(i)
    return str(value) + solve(permutation_value - i * permutation, values)


if __name__ == "__main__":
    print(solve(999999, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
