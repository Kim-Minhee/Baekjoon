N, M, K = map(int, input().split())
while K<0:
  K += N
M += (K-3)%N
if M>N:
  M %= N
print(M)