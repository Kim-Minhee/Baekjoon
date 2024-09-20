# 입력
K = input()

# 풀이
r = ''
for k in K:
  e = ord(k)-3
  if e<65:
    e += 26
  r += chr(e)

# 출력
print(r)