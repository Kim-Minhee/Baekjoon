import sys
input = sys.stdin.readline

N = int(input().strip())
A = [-1] + list(map(int, input().split()))
X1, D1 = input().split()
X2, D2 = input().split()

X1, X2 = int(X1), int(X2)
x1, x2 = 0, 0
for i, a in enumerate(A):
    if ((D1 == 'right' and i >= X1) or (D1 == 'left' and i <= X1)) and a > 0:
        x1 += a
    if ((D2 == 'right' and i >= X2) or (D2 == 'left' and i <= X2)) and a == 0:
        x2 += 1
print(x1, x2)