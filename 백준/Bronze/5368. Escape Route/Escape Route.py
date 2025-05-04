for _ in range(int(input())):
  M = int(input())

  s_row, s_col = int(), int()
  p = []
  for row in range(M):
    S = input()
    for col, s in enumerate(S):
      if s=='s':
        s_row, s_col = row, col
      elif s=='p':
        p.append((row, col))

  min_dist = float('inf')
  p_row, p_col = int(), int()
  for (row, col) in p:
    dist = ((s_row-row)**2+(s_col-col)**2)**0.5
    if dist<min_dist:
      p_row, p_col = row, col
      min_dist = dist

  print(f'({s_row},{s_col}):({p_row},{p_col}):{min_dist:.2f}')