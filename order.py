
num = 36726381

chars = []
for i in str(num):
    chars.append(i)
s = ""
chars.sort(reverse=True)

s = s.join(chars)
t = int(s)

print(t)
