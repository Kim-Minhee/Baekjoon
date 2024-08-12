# 입력
NAME = list(map(str, input().split('-')))

# 풀이
r = ''
for n in NAME:
  r += n[0]

# 출력
print(r)