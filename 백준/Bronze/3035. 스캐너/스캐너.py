r, c, zr, zc = map(int, input().split())
article = list()
for _ in range(r):
  a = list(input())
  article.append(a)

for i in range(r):
  for j in range(c):
    article[i][j] *= zc

for i in range(r):
  for _ in range(zr):
    print(''.join(article[i]))