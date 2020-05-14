n = 99999
n_s = list(map(int, str(n)))
n_len = len(n_s)

# encontrar o digito que é menor que o anterior
for d in range(n_len-1, 0, -1):
    if n_s[d] > n_s[d-1]:
        break

# se esse digito é 1, nada feito
if n<10:
    print(n)
    exit()

# olhar para a dta desse digito e encontrar o menor numero mas que seja maior que ele
n_new = n_s[d - 1]
small = d

for d_new in range(d + 1, n_len):
    #PyCharm simplicou-me n_s[d_new] > n_new and n_s[d_new] < n_s[small] para n_new < n_s[d_new] < n_s[small]:
    if n_new < n_s[d_new] < n_s[small]:
        small = d_new

# trocar de lugares com o numero encontrado
n_s[small], n_s[d - 1] = n_s[d - 1], n_s[small]

n_result = 0

for d_new in range(d):
    n_result = n_result * 10 + n_s[d_new]

n_s = sorted(n_s[d:])

for d_new in range(n_len - d):
    n_result = n_result * 10 + n_s[d_new]

if n_result <= n:
    print("-1")
print(n_result)

#tive ajuda em https://www.geeksforgeeks.org/find-next-greater-number-set-digits/
#uma solucao bruteforce:
# import itertools
# def next_bigger(n):
#     for num in sorted([int(''.join(map(str,x))) for x in list(set(itertools.permutations([int(x) for x in str(n)])))]):
#         if num>n:
#             return num
#     return -1

#https://www.codewars.com/kata/55983863da40caa2c900004e/solutions/python

##########https://www.codewars.com/kata/55983863da40caa2c900004e/train/python
