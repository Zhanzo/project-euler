from math import sqrt

def isPrime(number):
    if (number % 2 == 0):
        return False
    for i in range(3, round(sqrt(number))+1, 2):
        if (number % i == 0):
            return False
    return True

def main(max_primes):
    primes = [2, 3]
    number = 5
    while (len(primes) < max_primes):
        if (isPrime(number)):
            primes.append(number)
        number += 2;
    print(primes[len(primes)-1])

main(10001)
