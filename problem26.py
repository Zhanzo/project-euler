def find_cycle(number: int) -> int:
    current_remainder: int = 1 % number
    remainders: list[int] = [current_remainder]

    while True:
        current_remainder = current_remainder * 10 % number
        if current_remainder not in remainders:
            remainders.append(current_remainder)
        elif current_remainder == remainders[0]:
            return len(remainders)
        else:
            return 1

    return 0


def solve(number: int) -> int:
    longest_cycle: int = 0
    d: int = 0
    for i in range(2, number):
        cycle_length: int = find_cycle(i)
        if longest_cycle < cycle_length:
            longest_cycle = cycle_length
            d = i
    return d


if __name__ == "__main__":
    print(solve(1000))