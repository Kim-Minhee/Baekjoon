# 함수
def chk(n):
  r = True
  for i in range(2, n):
    if n%i==0:
      r = False
      break
  return r


# 입력
N = int(input())
L = list(map(int, input().split()))

# 풀이
cnt = 0
for l in L:
  if l!=1 and chk(l):
    cnt += 1

# 출력
print(cnt)