n = 999

p = 1
i = 0

while n > 9:
    for c in str(n):
        p = p * int(c)
    n = p
    p = 1
    i += 1
    print(i)

