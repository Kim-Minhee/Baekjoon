n, p = int(input()), 0
for _ in range(n):
  hm, d = map(str, input().split())
  h, m = map(int, hm.split(':'))
  d = int(d)
  if h>=7 and h<19:
    if h==18 and m+d>=60:
      p += (60-m)*10
      p += (d+m-60)*5
    else:
      p += d*10
  else:
    if h==6 and m+d>=60:
      p += (60-m)*5
      p += (d+m-60)*10
    else:
      p += d*5
print(p)