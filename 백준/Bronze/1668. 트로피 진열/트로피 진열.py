# 함수
def cntTrophy(t):
  c, m = 1, t[0]
  for h in t[1:]:
    if h>m:
      c += 1
      m = h
  return c

# 입력
N = int(input())
t = list()
for _ in range(N):
  H = int(input())
  t.append(H)

# 풀이
cnt1 = cntTrophy(t)
cnt2 = cntTrophy(list(reversed(t)))

# 출력
print(cnt1)
print(cnt2)