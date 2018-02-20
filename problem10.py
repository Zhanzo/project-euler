from math import sqrt

def isPrime(number):
    if (number % 2 == 0):
        return False
    for i in range(3, round(sqrt(number))+1, 2):
        if (number % i == 0):
            return False
    return True

def main(max):
    primes = [2, 3]
    for number in range(5, max, 2):
        if (isPrime(number)):
            primes.append(number)
    sum = 0        
    for prime in primes:
        sum += prime
    print(sum)

main(2000000)
