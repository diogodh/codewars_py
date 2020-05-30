year = 1705
#
# if year % 100 == 0:
#     print(int(year/100))
# else:
#     print(int(year/100)+1)

print(int(year/100) if year % 100 == 0 else int(year/100)+1)
