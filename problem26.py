import decimal


def find_cycle(number: int) -> int:
    found_remainders = [0 for _ in range(number)]
    value = 1
    index = 0

    while found_remainders[value] == 0 and value != 0:
        found_remainders[value] = index
        value *= 10
        value %= number
        index += 1

    return index - found_remainders[value]


def solve(limit: int) -> int:
    longest_cycle: int = 0
    max_d: int = 0

    for d in range(2, limit):
        cycle_length: int = find_cycle(d)

        if longest_cycle < cycle_length:
            longest_cycle = cycle_length
            max_d = d

    return max_d


if __name__ == "__main__":
    print(solve(1000))
