n = int(input())
num = list(map(int, input().split()))
for s in num:
  if sum(num)==s*2:
    print(num.index(s)+1)
    break