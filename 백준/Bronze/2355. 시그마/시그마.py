# 입력
A, B = map(int, input().split())

# 풀이
r = (A+B)*(abs(B-A)+1)/2

# 출력
print(int(r))