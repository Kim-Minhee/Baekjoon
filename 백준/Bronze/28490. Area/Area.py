n = int(input())
area = list()
for _ in range(n):
  h, w = map(int, input().split())
  area.append(h*w)
print(max(area))