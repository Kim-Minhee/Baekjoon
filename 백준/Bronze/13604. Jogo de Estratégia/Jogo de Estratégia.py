import sys
input = sys.stdin.readline

J, R = map(int, input().split())
A = list(map(int, input().split()))
max_score = -1
winner = -1
for i in range(J):
    score = sum(A[i::J])
    if score >= max_score:
        max_score = score
        winner= i + 1
print(winner)