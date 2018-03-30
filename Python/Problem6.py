def squareSum(n):
    square_sum = 0
    for i in range(1, n+1):
        square_sum += i
    square_sum *= square_sum
    return square_sum

def sumSquares(n):
    sum_squares = 0
    for i in range(1, n+1):
        sum_squares += (i*i)
    return sum_squares

def main(n):
    square_sum = squareSum(n)
    sum_squares = sumSquares(n)
    print(square_sum - sum_squares)

main(100)
