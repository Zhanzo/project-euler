def isPalindrome(number):
    digits = []
    while (number > 0):
        digits.append(number % 10)
        number = number // 10
    for i in range (0, len(digits)):
        if (digits[i] != digits[len(digits)-1-i]):
            return False
    return True

def main():
    max_prod = 0
    for i in range(1, 1000):
        for j in range(1, 1000):
            if ((isPalindrome(i*j)) and (i*j > max_prod)):
                max_prod = i*j
    print(max_prod)

main()
