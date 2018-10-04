def main(num_digits):
    index = fibonacci(num_digits)
    print(index)

def fibonacci(num_digits):
    x = 0
    y = 1
    z = 0
    index = 1
    while (len(str(z)) < num_digits):
        z = x + y
        temp = y
        y = x + y
        x = temp
        index += 1
    print(z)
    return index

main(1000)