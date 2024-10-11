# 입력
A, B = map(str, input().split())

# 풀이
h = []
if len(A)<len(B):
  A, B = B, A
for i in range(len(B)):
  h.append(str(int(A[-i-1])+int(B[-i-1])))
h.reverse()

r = ''
if len(A)!=len(B):
  l = len(A)-len(B)
  r += A[:l]
r += ''.join(h)

# 출력
print(r)