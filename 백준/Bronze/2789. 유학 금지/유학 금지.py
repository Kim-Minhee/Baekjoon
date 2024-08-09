# 입력
S = input()

# 풀이
r = ''
for s in S:
  if s not in ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']:
    r += s

# 출력
print(r)