A = int(input())
r = 1
if A>1:
    r += 4 * (4 ** (A - 1) - 1) // 3
print(r % 500000009)