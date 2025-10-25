import sys
input = sys.stdin.readline

N, K = map(int, input().split())

days = [0, 1]
holiday = set(int(input()) for _ in range(K))

for i in range(2, N + 1):
    if days[i - 1] == 0 or i in holiday:
        days.append(1)
    else:
        days.append(0)

print(sum(days))