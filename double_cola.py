names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
r = 74

while r > len(names):
    r = (r - len(names)+1) // 2
print(names[r-1])

# A magia é esta: a sequencia 1, repete-se duplicada no 6 e depois no 16. Se eu pegar numa seq, por ex a 20, tirar 4 dá
# 16 e dividir por 2, dá 8. A seq 20 é a seq 8 duplicada. Ou seja, a seq repete-se duplicada a cada x * 2 + 4

#(y - 4) / 2 = x »» x * 2 + 4 = y

#50 - 4 = 44, dividir por 2 dá 22. 22 - 4 = 18 / 2 dá 9. 9-4 = 5. 5 / 2 dá 2 (o excesso n conta!) 50»22»9»2
#é engraçado q a seq funciona a descer mas nao a subir qd o resultado é impar.


# 1 » 12345
# 2 » 234511
# 3 » 3451122
# 4 » 45112233
# 5 » 511223344
# 6 » 1122334455
# 7 » 12233445511
# 8 » 223344551111
# 9 » 2334455111122
# 10» 33445511112222
# 11» 344551111222233
# 12» 4455111122223333
# 13» 45511112222333344
# 14» 551111222233334444
# 15» 5111122223333444455
# 16» 11112222333344445555
# 17» 111222233334444555511
# 18» 1122223333444455551111
# 19» 12222333344445555111111
# 20» 222233334444555511111111
# 21» 2223333444455551111111122
# 22» 22333344445555111111112222

# LOGIC
# Let's call for simplicity the people a,b,c,d and e. Then it is not too hard to see they will come on the following order:
# a, b, c, d, e
# a,a, b,b, c,c, d,d, e,e (twice each)
# a,a,a,a, b,b,b,b, c,c,c,c, d,d,d,d, e,e,e,e (4 times each)
#
# Then 8 times each, etc.
#
# Informal proof: Suppose each time a person get a cola, he is created as a double person not in the end of line, but rather in a separate row. When the line is over, this row becomes the new line. Then the (k+1)-th row is created by all people in the k-th row "doubling" themselves, at the same order.
#
# Now, suppose you want to find the n-th person, and suppose n is in the k-th row. By subtracting 4 and dividing by 2 you simply move to the same person in the (k-1)th row. You do that iteratively until you get to the first row.

# y = x + 4
# number os each name in list = r + 4

# items = r + 4
# items_double = items % 5
# print(items_double)
#
# i = 0
# r -= 1
# while i < r:
#     names.append(names[0])
#     names.append(names.pop(0))
#     i += 1
# print(names)
# print(names[0])
#

# too much memory for huge numbers » needed to improve math
# r = 16
# i = 0
# while i < r - 1:
#     names.append(names[0])
#     names.append(names.pop(0))
#     i += 1
# print(names)

# Old training
# import math
# x = 30000000
# x = x + 4
#
# y = int(x/5)
# z = int(math.log2(y))
# zz = pow(2, z)
#
# print(z)
# print(zz)
# excess = x - (zz * 5)
#
# print(excess)

#
# 1         = 5
# 6 (x2)    = 10
# 16 (x4)   = 20
# 36 (x8)   = 40
# 76 (x16)  = 80
#
#
