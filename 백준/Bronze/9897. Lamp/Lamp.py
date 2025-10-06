import sys
input = sys.stdin.readline

L, G, R = map(int, input().split())
lights = [False] * L

guards = {}
for _ in range(G):
    N, A, D = input().split()
    guards[N] = (int(A), int(D))

seq = [input().strip() for _ in range(R)]

for i in range(R):
    a, d = guards[seq[i]]
    for j in range(a - 1, L, d):
        if lights[j]:
            lights[j] = False
        else:
            lights[j] = True
print(lights.count(True))