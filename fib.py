
prod = 4895
z = 2
1 + 0

while (z * z - 1) < prod:
    f = z - 1 + z - 2
    a = z - 1
    b = z - 2
    z = a + b
    print(z)

#F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.


