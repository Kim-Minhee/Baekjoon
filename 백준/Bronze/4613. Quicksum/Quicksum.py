while True:
  S = input()
  if S=='#': break

  quicksum = 0
  for i, s in enumerate(S):
    if s!=' ':
      quicksum += (i+1)*(ord(s)-64)
  print(quicksum)