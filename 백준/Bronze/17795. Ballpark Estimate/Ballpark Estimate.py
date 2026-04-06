import sys
input = sys.stdin.readline

N = input().strip()
l = len(N)
a = int(N[0] + '0' * (l - 1))
b = a + 10 ** (l - 1)
N = int(N)
close_a, close_b = abs(N - a), abs(N - b)
if close_a < close_b:
    print(a)
elif close_a == close_b:
    print(max(a, b))
else:
    print(b)