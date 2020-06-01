integer = 17
r = []
i = 2

while i <= integer / 2:
    if integer % i == 0:
        r.append(i)
    i += 1

if not r:
    print(str(integer) + " is prime")
else:
    print(r)
