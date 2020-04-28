n = 493193
k = 0

while len(str(n)) > 1:
    for char in str(n):
        k += int(char)
    n = k
    char = k = 0
print(n)

#print(n%9 or n and 9)
