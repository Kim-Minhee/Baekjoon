N = int(input())

mi = N*2+1
r = [1, 1, N]
for a in range(1, N+1):
  if N%a==0:
    t = N//a
    for b in range(1, t+1):
      if t%b==0:
        c = t//b
        if a*b+b*c+c*a<mi:
          mi = a*b+b*c+c*a
          r = [a, b, c]
print(*r)