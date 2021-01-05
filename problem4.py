def reverse_string(string: str) -> str:
    return string[::-1]


def is_palindrome(number: str) -> bool:
    number_reverse: str = reverse_string(number)
    return number == number_reverse


def solve(start: int, stop: int) -> int:
    max_product: int = 0
    for i in range(start, stop):
        for j in range(start, stop):
            product: int = i * j
            if is_palindrome(str(product)) and product > max_product:
                max_product = product
    return max_product


if __name__ == "__main__":
    print(solve(100, 1000))
