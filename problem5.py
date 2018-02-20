def isDivisible(n):
    for i in range(1, 21):
        if (n % i != 0):
            return False
    return True

def main():
    i = 20
    while (not isDivisible(i)):
        i +=20
    print(i)

main()
