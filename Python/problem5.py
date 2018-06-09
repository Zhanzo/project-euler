def isDivisible(n):
    for i in range(1, 21):
        if (n % i != 0):
            return False
    return True

def main():
    smallest_multiple = 20
    while (not isDivisible(smallest_multiple)):
        smallest_multiple +=20
    print(smallest_multiple)

main()
