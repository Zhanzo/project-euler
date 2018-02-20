def findTriplet(sum):
    for a in range(1, sum-1):
        for b in range(a+1, sum):
            for c in range(b+1, sum+1):
                if (a + b + c == sum):
                    if (isPythagorean(a, b, c)):
                        return a*b*c
    return 0

def isPythagorean(a, b, c):
    sum = (a**2) + (b**2)
    if (sum == c**2):
        return True
    else:
        return False

def main(sum):
    print(findTriplet(sum))
    
main(1000)
