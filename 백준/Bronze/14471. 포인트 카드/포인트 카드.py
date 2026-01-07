import sys
input = sys.stdin.readline

N, M = map(int, input().split())
need_money = []
for _ in range(M):
    A, B = map(int, input().split())
    if A >= N:
        continue
    else:
        need_money.append(N - A)
if len(need_money) <= 1:
    print(0)
else:
    need_money.sort()
    print(sum(need_money[:-1]))