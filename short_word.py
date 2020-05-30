s = "bitcoin take over the world maybe who knows perhaps"

n = len(s)

for w in s.split():
    while len(w) < n:
        n = len(w)

print(n)