for _ in range(int(input())):
  N = int(input())
  l = list(map(int, input().split()))
  l.sort()
  print(l[0], l[-1])