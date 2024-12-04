# 입력
N = int(input())
S = list(map(int, input().split()))

# 풀이
S.sort()

# 출력
print(S[-1]-S[0])