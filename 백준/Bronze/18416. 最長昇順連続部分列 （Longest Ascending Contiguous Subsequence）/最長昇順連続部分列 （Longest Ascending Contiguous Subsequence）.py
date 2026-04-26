# GPT 5
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

cur = 1
ans = 1

for i in range(1, N):
    if A[i] >= A[i-1]:
        cur += 1
    else:
        cur = 1
    ans = max(ans, cur)

print(ans)