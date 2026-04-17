# GPT 5
import sys
input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)]

A.sort()

room = 1
i = 0
ans = 0

while room <= N and i < N:
    if A[i] == room:
        ans += 1
        room += 1
        i += 1
    elif A[i] < room:
        i += 1
    else:
        room += 1

print(ans)