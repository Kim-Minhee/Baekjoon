# 입력
for i in range(int(input())):
  A, B = list(input()), list(input())
  
  # 풀이
  a, b = len(A), len(B)
  for j in A:
    if j in B:
      B.remove(j)
  r = a-b+2*len(B)

  # 출력
  print(f'Case #{i+1}: {r}')