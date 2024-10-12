for _ in range(int(input())):
  # 입력
  T = input()

  # 풀이
  total, cnt = 0, 0
  for i in range(len(T)):
    if T[i]=='O':
      cnt += 1
      if i==len(T)-1:
        total += cnt*(cnt+1)//2
    else:
      total += cnt*(cnt+1)//2
      cnt = 0

  # 출력
  print(total)