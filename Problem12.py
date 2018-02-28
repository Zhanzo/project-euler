for i in range(1, 100000000):
    c = 0
    for b in range(1, i+1):
        c += b
        k = 0
        for d in range(1, b+1):
            if b % d == 0:
                k += 1
            if k == 500:
                print(b)
        
        
        
