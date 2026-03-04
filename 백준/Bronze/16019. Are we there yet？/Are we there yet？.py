import sys
input = sys.stdin.readline

D = [0] + list(map(int, input().split()))
dist = []
for i in range(5):
    dist.append(sum(D[:i + 1]))
for i in range(5):
    for j in range(5):
        print(abs(dist[i] - dist[j]), end = ' ')
    print()