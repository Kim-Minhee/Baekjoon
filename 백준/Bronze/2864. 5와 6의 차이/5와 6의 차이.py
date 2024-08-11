# 입력
A, B = map(str, input().split())

# 풀이
min_a = int(A.replace('6', '5'))
min_b = int(B.replace('6', '5'))
max_a = int(A.replace('5', '6'))
max_b = int(B.replace('5', '6'))

# 출력
print(min_a+min_b, max_a+max_b)