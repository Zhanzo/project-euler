
i = 98
s = 100*99

while i > 0:
    s = s * (100*i)
    i -= 1
print(s)

n = str(s)
s2 = 0

for item in n:
    s2 += int(item)
print(s2)
