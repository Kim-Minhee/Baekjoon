# 함수
def reward(lst):
  d = dict()
  for i in lst:
    if i not in d.keys():
      d[i] = 1
    else:
      d[i] += 1
  l = len(d.keys())
  if l==4:
    r = max(d.keys())*100
  elif l==3:
    for k, v in d.items():
      if v==2:
        r = 1000+k*100
        break
  elif l==2:
    if 2 in d.values():
      r = 2000+(sum(d.keys()))*500
    else:
      for k, v in d.items():
        if v==3:
          r = 10000+k*1000
          break
  else:
    r = 50000+list(d.keys())[0]*5000
  return r


# 입력
N = int(input())
r = list()
for _ in range(N):
  D = list(map(int, input().split()))

  # 풀이
  r.append(reward(D))

# 출력
print(max(r))