import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
r = 1
cur_page = 0
for a in A:
    if a <= K - cur_page:
        cur_page += a
    else:
        cur_page = a
        r += 1
print(r)