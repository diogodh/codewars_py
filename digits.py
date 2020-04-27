import timeit

n = 46288
p = 3
k = 0
#n_str = str(n)

for i in str(n):
    k += pow(int(i), p)
    p += 1

if k % n == 0:
    print(k //n)
else:
    print("None")
