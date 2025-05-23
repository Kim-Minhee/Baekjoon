def encode(N, S):
  return S[N:]+S

for _ in range(int(input())):
  N, C, S = input().split()
  
  N = int(N)
  for _ in range(int(C)):
    S = encode(N, S)
  print(S)