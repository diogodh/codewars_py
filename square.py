num = 9119
final = ""

for c in str(num):
    final += str(int(c) ** 2)
print(int(final))