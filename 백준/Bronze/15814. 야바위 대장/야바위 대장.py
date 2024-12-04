# 입력
S = list(input())

# 풀이
for _ in range(int(input())):
  A, B = map(int, input().split())
  S[A], S[B] = S[B], S[A]

# 출력
print(''.join(S))