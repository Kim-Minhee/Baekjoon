# GPT
tris = [0, 0, 0, 0]

try:
    while True:
        values = list(map(int, input().split()))
        values.sort()
        a, b, c = values

        if a + b <= c:
            break

        tris[0] += 1
        s = a ** 2 + b ** 2
        if s == c ** 2:
            tris[1] += 1
        elif s > c ** 2:
            tris[2] += 1
        else:
            tris[3] += 1

except EOFError:
    pass

print(*tris)