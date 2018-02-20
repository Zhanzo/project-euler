from math import sqrt

def isPrime(number):
    if (number % 2 == 0):
        return False
    for i in range(3, round(sqrt(number))+1, 2):
        if (number % i == 0):
            return False
    return True

def main():
    number = 600851475143
    max_factor = 0

    for i in range (3, round(sqrt(number))+1, 2):
        if (number % i == 0):
            if (isPrime(i)):
                max_factor = i

    print(max_factor)

main()
