import sys
input = sys.stdin.readline

x, y = set(), set()
for _ in range(int(input().strip())):
    X, Y = map(int, input().split())
    x.add(X)
    y.add(Y)

l = max(max(x) - min(x), max(y) - min(y))
print(l * l)