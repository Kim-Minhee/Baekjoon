# GPT
import bisect

N, Q = map(int, input().split())

# 누적합 저장
prefix = [0]
for _ in range(N):
    B = int(input())
    prefix.append(prefix[-1] + B)

# 각 T에 대해 이진 탐색
for _ in range(Q):
    T = int(input())
    note_index = bisect.bisect_right(prefix, T) - 1
    print(note_index + 1)