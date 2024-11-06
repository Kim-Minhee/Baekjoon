for _ in range(int(input())):
  # 입력
  C, D, CP, P = map(str, input().split())

  # 풀이
  d = {'R':0.55, 'G':0.7, 'B':0.8, 'Y':0.85, 'O':0.9, 'W':0.95}
  c = float(C)*d[D]
  if CP=='C':
    c *= 0.95
  if P=='C':
    c *= 100
    if c%10>5:
      c += 10
    c -= c%10
    c /= 100
  
  # 출력
  print('${:.2f}'.format(c))