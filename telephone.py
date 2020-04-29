n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
"(123) 456-7890"

i = 0
n.insert(0, "(")
i += 1

n.insert(3 + i, ")")
i += 1

n.insert(3 + i, " ")
i += 1

n.insert(6 + i, "-")
i += 1

n_str = ''.join(str(e) for e in n)
