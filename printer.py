s = "aaaxbbbbyyhwawiwjjjwwm"
i = j = 0

for char in s:
    if char > "m":
        i += 1

final = str(i) + "/" + str(len(s))
print(final)
