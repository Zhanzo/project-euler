def solve(num_digits: int) -> int:
    fibonacci_numbers: list[int] = [1, 1]
    while len(str(fibonacci_numbers[-1])) < num_digits:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    return len(fibonacci_numbers)


if __name__ == "__main__":
    print(solve(1000))