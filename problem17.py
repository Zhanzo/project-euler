def solve() -> int:
    single_digits: list[int] = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    double_digits: list[int] = [
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ]
    double_digits2: list[int] = [
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]
    hundred: int = len("hundred") * 9
    hundred_and: int = len("hundredand") * 9 * 99

    single_digit_sum: int = sum(len(i) for i in single_digits)
    double_digit_sum1: int = sum(len(i) for i in double_digits)
    double_digit_sum2: int = (
        10 * sum(len(i) for i in double_digits2) + 8 * single_digit_sum
    )
    single_and_double_sum: int = (
        single_digit_sum + double_digit_sum1 + double_digit_sum2
    )

    triple_digits: int = (
        single_digit_sum * 100 + single_and_double_sum * 9 + hundred + hundred_and
    )

    return single_and_double_sum + triple_digits + len("onethousand")


if __name__ == "__main__":
    print(solve())
