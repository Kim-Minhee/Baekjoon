import sys
input = sys.stdin.readline

N, M = int(input()), int(input())

score = [0]*N
A = list(map(int, input().split()))
for i in range(M):
    B = list(map(int, input().split()))
    
    target = A[i]
    wrong = 0
    for j, answer in enumerate(B):
        if answer == target:
            score[j] += 1
        else:
            wrong += 1
    score[target - 1] += wrong

for s in score:
    print(s)