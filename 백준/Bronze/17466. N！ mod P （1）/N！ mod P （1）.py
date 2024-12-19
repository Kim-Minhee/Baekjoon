# A*B%C = ((A%C)*(B%C))%C
import sys

N, P = map(int, sys.stdin.readline().split())

r = 1
for i in range(2, N+1):
  r = (r*i)%P # r과 i는 P보다 작음
print(r)