s = 'abcdddddddddddddd'
i = 0
j = []
if len(s) / 2 == int(len(s) / 2):
    print("é par")
else:
    s = s + "_"

while i < len(s):
      j.append(s[i] + s[i+1])
      i += 2
print(j)

#solution('abc') # should return ['ab', 'c_']