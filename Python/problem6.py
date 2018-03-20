def squareSum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    sum = sum*sum
    return sum

def sumSquares(n):
    sum = 0
    for i in range(1, n+1):
        sum += (i*i)
    return sum

def main(n):
    square_sum = squareSum(n)
    sum_squares = sumSquares(n)
    print(square_sum - sum_squares)

main(100)
