import sys
input = sys.stdin.readline

N, M = map(int, input().split())
sum_dict = {}
for n in range(1, N + 1):
    for m in range(1, M + 1):
        sum_dict[n + m] = sum_dict.get(n + m, 0) + 1

r = []
max_cnt = max(sum_dict.values())
for num, cnt in sum_dict.items():
    if cnt == max_cnt:
        r.append(num)
for num in sorted(r):
    print(num)