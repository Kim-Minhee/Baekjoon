# 입력
L, N = input(), input()

# 풀이
score = 0
for n in N:
  score += ord(n)-64

# 출력
print(score)