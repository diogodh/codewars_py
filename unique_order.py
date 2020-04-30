iterable = 'AAAABBBCCDAABBB'
result = []

for i in iterable:
    result.append(i)

i = 0

try:
    while i <= len(result):
        if result[i] == result[i+1]:
            result.pop(i+1)
            i = i - 1
        i += 1
except:
    print(result)