import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
pairs = set()
for n in A:
    if K - n in A:
        pairs.add((n, K - n))
print(len(pairs) // 2)