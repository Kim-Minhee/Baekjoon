# 입력
s = list(map(int, input().split()))

# 풀이
a = [1, 2, 3, 4, 5, 6, 7, 8]
if s==a:
  r = 'ascending'
elif s==a[::-1]:
  r = 'descending'
else:
  r = 'mixed'

# 출력
print(r)