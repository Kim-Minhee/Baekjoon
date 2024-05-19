def Tcnt(num, T):
  if num%T==0:
    return num//T
  else:
    return num//T+1

N = int(input())
S = list(map(int, input().split()))
T, P = map(int, input().split())
t = 0
for s in S:
  t += Tcnt(s, T)
p1, p2 = N//P, N%P
print(t)
print(p1, p2)