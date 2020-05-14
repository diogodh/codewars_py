import math

n = 1977326743
i = 0
limit = int(math.sqrt(n)) + 1
x = list(range(2, limit))
xl = len(x) - 1
r = []
for item in x:
    print(item)
    while i <= xl:
        if pow(item, x[i]) == n:
            r.append(item)
            r.append(x[i])
            print(r)
            exit()
        else:
            i += 1
    i = 0
print("Nops")