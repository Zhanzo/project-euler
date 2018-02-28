i = 6
c = 10
while i < 2000000:
    print(i)
    d = 0
    a = 2
    while a < i:
        if i % a == 0:
            d += 1
            break
        a += 1
    if d == 0:
        c += i
    i += 1
print(c)
