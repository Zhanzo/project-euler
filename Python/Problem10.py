from math import sqrt

def isPrime(number):
    for i in range(3, round(sqrt(number))+1, 2):
      if (number % i == 0):
        return False
    return True

def main():
    sum = 5
    for number in range(5, 2000000, 2):
      if (isPrime(number)):
        sum += number
    print(sum)

main()
