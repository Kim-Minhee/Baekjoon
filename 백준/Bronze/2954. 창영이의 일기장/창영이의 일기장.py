# 함수
def decoding(string):
  gather = ['a', 'e', 'i', 'o', 'u']
  r = ''
  for i, s in enumerate(string):
    r += s
    if s in gather:
      if i+2!=len(string):
        r += decoding(string[i+3:])
        return r
  return r

# 입력
S = list(map(str, input().split()))

# 풀이
r = list()
for s in S:
  r.append(decoding(s))

# 출력
print(*r)