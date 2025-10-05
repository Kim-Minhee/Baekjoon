import sys
input = sys.stdin.readline

X, Y = map(int, input().split())
x, y = format(X, '016b'), format(Y, '016b')

morton = ''
for i in range(32):
    if i % 2 == 0:
        morton += x[i // 2]
        # print(x[i // 2])
    else:
        morton += y[i // 2]
print(int(morton, 2))