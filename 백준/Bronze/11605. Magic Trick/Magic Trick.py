import sys
input = sys.stdin.readline

ops = []
xs = []
for _ in range(int(input().strip())):
    OP, X = input().split()
    ops.append(OP)
    xs.append(int(X))

cnt = 0
for i in range(1, 101):
    for op, x in zip(ops, xs):
        if op == 'ADD':
            i += x
        elif op == 'SUBTRACT':
            i -= x
        elif op == 'MULTIPLY':
            i *= x
        else:
            i /= x
        if i < 0 or i % 1 != 0:
            cnt += 1
            break
print(cnt)