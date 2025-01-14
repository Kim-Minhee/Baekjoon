titles, levels = [], []

for _ in range(int(input())):
  title, level = input().split()
  titles.append(title)
  levels.append(level)

print(titles[levels.index(min(levels))])