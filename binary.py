n = 1234

n = str("{0:b}".format(n))
n2 = 0

for char in n:
    n2 = n2 + int(char)

print(n2)

# Simpler way
#   n = "{0:b}".format(n)
# print(n.count("1"))