K = int(input())

icons = ['*x*', ' xx', '* *']
for icon in icons:
  icon_k = icon[0]*K + icon[1]*K + icon[2]*K
  for _ in range(K):
    print(icon_k)