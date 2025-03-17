while True:
  S = input().split()
  if S[0]=='#': break
  for s in S:
    print(s[::-1], end=' ')