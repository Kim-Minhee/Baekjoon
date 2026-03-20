import sys
input = sys.stdin.readline

milk = []
buckets = []
for _ in range(3):
    C, M = map(int, input().split())
    buckets.append(C)
    milk.append(M)

for i in range(100):
    cur, next = i % 3, (i + 1) % 3
    milk[next] += milk[cur]
    if milk[next] > buckets[next]:
        milk[cur] = milk[next] - buckets[next]
        milk[next] -= milk[cur]
    else:
        milk[cur] = 0

for m in milk:
    print(m)