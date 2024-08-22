# 입력
M = input()

# 풀이
b = [1, 0, 0]
for m in M:
  if m=='A':
    b[0], b[1] = b[1], b[0]
  elif m=='B':
    b[1], b[2] = b[2], b[1]
  elif m=='C':
    b[0], b[2] = b[2], b[0]

# 출력
print(b.index(1)+1)