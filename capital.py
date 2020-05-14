string = "How can mirrors be real if our eyes aren't real"
a = ""

for w in string.split():
    a = a + w[0].upper() + w[1:] + " "
a = a.rstrip()
# minimal b = [w[0].upper() + w[1:] for w in string.split()] // a = b.join(a)

print(a)