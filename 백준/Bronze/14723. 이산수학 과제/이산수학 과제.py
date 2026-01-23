import sys
input = sys.stdin.readline

N = int(input().strip())
n = 1
a_list = [1]
b_list = [1]
while len(a_list) < N:
    n += 1
    a_list += [a for a in range(n, 0, -1)]
    b_list += [b for b in range(1, n + 1)]
print(a_list[N - 1], b_list[N - 1])