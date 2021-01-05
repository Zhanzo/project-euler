
def main(number):
    faculty = get_faculty(number)
    digit_sum = sum_digits(faculty)
    print(digit_sum)

def sum_digits(number):
    digit_sum = 0
    while (number > 0):
        digit_sum += number%10
        number //= 10
    return digit_sum

def get_faculty(number):
    faculty = 1
    while (number > 0):
        faculty *= number
        number -= 1
    return faculty

main(100)