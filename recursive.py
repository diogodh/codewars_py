n = 132189
j = 0
for i in str(n):
    j = int(i)
    j = i + j

    k += pow(int(i), p)
    p += 1

if k % n == 0:
    print(k //n)
else:
    print("None")
