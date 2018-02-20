def main():
    i = 1
    j = 2
    sum = 2
    while (j < 4000000):
        k = i+j
        i = j
        j = k
        if (j % 2 == 0):
            sum += j

    print(sum)

main()
