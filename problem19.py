def calc_sundays(stop_year: int) -> int:
    num_sundays: int = 0
    day: int = 2
    month: int = 1
    year: int = 1901
    date: int = 1

    while year < stop_year:
        if day == 6 and date == 1:
            num_sundays += 1

        if month == 2 and year % 4 != 0 and date == 28:
            month += 1
            date = 1
        elif month == 2 and date == 29:
            month += 1
            date = 1
        elif (month == 4 or month == 6 or month == 9 or month == 11) and date == 30:
            month += 1
            date = 1
        elif (
            month == 1
            or month == 3
            or month == 5
            or month == 7
            or month == 8
            or month == 10
        ) and date == 31:
            month += 1
            date = 1
        elif month == 12 and date == 31:
            year += 1
            month = 1
            date = 1
        else:
            date += 1

        day = (day + 1) % 7

    return num_sundays


if __name__ == "__main__":
    print(calc_sundays(2001))
