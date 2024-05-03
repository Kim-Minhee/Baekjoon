cnt = 0
for _ in range(int(input())):
  a, b, c = map(int, input().split())
  if a+b+c!=-3:
    if (b+c==-2 and a>=0) or (c==-1 and a>=0 and b>=a) or (a>=0 and b>=a and c>=b):
      cnt += 1
print(cnt)