L, R, A = map(int, input().split())
s, b = min(L, R), max(L, R)
a = min(A, b-s)
s += a
A -= a
r = s*2
r += A//2*2
print(r)