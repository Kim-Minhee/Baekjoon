for _ in range(int(input())):
  # 입력
  S = input()

  # 풀이
  cnt = {}
  for s in S:
    if s!=' ' and s not in cnt.keys():
      cnt[s] = 1
    elif s!=' ':
      cnt[s] += 1
  max_cnt = max(cnt.values())
  if list(cnt.values()).count(max_cnt)!=1:
    print('?')
  else:
    for key, value in cnt.items():
      if value==max_cnt:
        print(key)
        break