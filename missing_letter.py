dic = ["a", "b", "c", "d" , "e" , "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
chars = ['O','Q','R','S']
z, i, x = 0, 0, 0

if chars[0].istitle():
    z = 1
    dic = [element.upper() for element in dic]

while chars[x] != dic[i]:
    i += 1
for item in chars:
    if chars[x] != dic[i]:
        if z == 1:
            print(dic[i])
        else:
            print(dic[i].lower())
            break
    i += 1
    x += 1
