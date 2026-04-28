import sys
input = sys.stdin.readline

N, M = map(int, input().split())
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:M]
r = 0
for _ in range(N):
    W = list(input().strip())
    if len(set(W)) != len(W):
        continue
    check = True
    for w in W:
        if w not in alpha:
            check = False
            break
    if check:
        r += 1
print(r)