import string

lower = [i for i in string.ascii_lowercase]
upper = [i for i in string.ascii_uppercase]
num = [str(i) for i in range(10)]

while 1:
  try:
    # 입력
    S = input()

    if S=='':
      break

    # 풀이
    cnt = [0, 0, 0, 0]
    for s in S:
      if s in lower:
        cnt[0] += 1
      elif s in upper:
        cnt[1] += 1
      elif s in num:
        cnt[2] += 1
      else:
        cnt[3] += 1

    # 출력
    print(* cnt)
  except:
    break