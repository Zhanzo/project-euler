def isPalindrome(number):
    list = []
    while (number > 0):
        list.append(number % 10)
        number = number // 10
    for i in range (0, len(list)):
        if (list[i] != list[len(list)-1-i]):
            return False
    return True

def main():
    max = 0
    for i in range(1, 1000):
        for j in range(1, 1000):
            if ((isPalindrome(i*j)) and (i*j > max)):
                max = i*j
    print(max)

main()
