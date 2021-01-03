def solve(max_start_number: int) -> int:
    collatz_lengths: list[int] = [0 for _ in range(max_start_number + 1)]
    for number in range(1, max_start_number):
        num_terms: int = calc_terms(number, collatz_lengths)
        collatz_lengths[number] = num_terms
    return collatz_lengths.index(max(collatz_lengths))


def calc_terms(number: int, collatz_lengths: list[int]) -> int:
    num_terms: int = 0
    n: int = number
    while n > 1 and n >= number:
        n = collatz(n)
        num_terms += 1
    return num_terms + collatz_lengths[n]


def collatz(number: int) -> int:
    if number % 2 == 0:
        return number // 2
    return number * 3 + 1


if __name__ == "__main__":
    print(solve(1000000))
