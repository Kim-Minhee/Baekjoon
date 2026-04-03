import sys
input = sys.stdin.readline

N = int(input().strip())
S = input().rstrip()

bonus = 0
score = 0
for i, s in enumerate(S):
    if s == 'O':
        score += i + 1 + bonus
        bonus += 1
    else:
        bonus = 0
print(score)