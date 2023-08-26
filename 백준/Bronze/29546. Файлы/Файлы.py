n = int(input())
files = list()
for _ in range(n):
  files.append(input())
m = int(input())
for _ in range(m):
  f, s = map(int, input().split())
  for i in range(f-1, s):
    print(files[i])