import sys
input = sys.stdin.readline

N = int(input().strip())
X = list(map(int, input().split()))
M = int(input().strip())
A = list(map(int, input().split()))

board = [0] * max(X)
for i in X:
    board[i - 1] = 1

for j in A:
    x = X[j - 1] + 1
    if x not in X and x < 2020:
        X[j - 1] += 1

for x in X:
    print(x)