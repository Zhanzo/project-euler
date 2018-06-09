def main():
    lower = 1
    upper = 2
    sum_even = 2
    while (j < 4000000):
        sum_lower_upper = i+j
        lower = upper
        upper = sum_lower_upper
        if (j % 2 == 0):
            sum_even += j

    print(sum_even)

main()
