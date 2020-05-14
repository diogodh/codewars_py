import math

n = 5
i = 2
r = []

while i < n:
    if i ** int(round(math.log(n, i))) == n:
        j = int(round(math.log(n, i)))
        r.append(i)
        r.append(j)
        exit()
    i += 1
print("None")

