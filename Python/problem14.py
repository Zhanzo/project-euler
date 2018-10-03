def main(max_number):
    max_terms = 0
    max_collatz = 0
    for i in range(max_number):
        num_terms = calc_terms(i)
        if (num_terms > max_terms):
            max_terms = num_terms
            max_collatz = i
    print(max_collatz)

def calc_terms(number):
    num_terms = 1
    while (number > 1):
        number = collatz(number)
        num_terms += 1
    return num_terms

def collatz(number):
    if (number % 2 == 0):
        return number//2
    else:
        return 3 * number + 1

main(1000000)
