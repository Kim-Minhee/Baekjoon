import sys
input = sys.stdin.readline

N, M = map(int, input().split())
front, back = [], []
for _ in range(N):
    A, B = map(int, input().split())
    front.append(A)
    back.append(B)

cur = front.copy()
for _ in range(M):
    K = int(input().strip())
    for idx, num in enumerate(cur):
        if num <= K:
            if num == front[idx]:
                cur[idx] = back[idx]
            else:
                cur[idx] = front[idx]

print(sum(cur))