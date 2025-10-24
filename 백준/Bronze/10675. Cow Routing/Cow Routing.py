import sys
input = sys.stdin.readline

A, B, N = map(int, input().split())
costs = []
for _ in range(N):
    COST, CNT = map(int, input().split())
    ROUTE = list(map(int, input().split()))
    if A in ROUTE and B in ROUTE:
        if ROUTE.index(A) < ROUTE.index(B):
            costs.append(COST)
if len(costs) == 0:
    print(-1)
else:
    print(min(costs))