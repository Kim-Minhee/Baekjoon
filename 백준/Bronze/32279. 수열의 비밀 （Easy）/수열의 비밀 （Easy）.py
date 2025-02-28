N = int(input())
P, Q, R, S = map(int, input().split())
A = [int(input())]
s = A[0]

for i in range(1, N):
  if i%2==1:
    a_2i = P*A[i//2]+Q
  else:
    a_2i = R*A[i//2-1]+S
  A.append(a_2i)
  s += a_2i

print(s)