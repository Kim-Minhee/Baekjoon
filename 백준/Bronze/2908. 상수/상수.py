# 입력
A, B = map(str, input().split())

# 풀이
a = A[::-1]
b = B[::-1]

# 출력
print(max(a, b))