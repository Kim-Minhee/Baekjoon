import sys
input = sys.stdin.readline

G = list(map(int, input().split()))
E = list(map(int, input().split()))

g_avg = sum(G) / 2
e_avg = sum(E) / 2

if g_avg == e_avg:
    print('Tie')
elif g_avg > e_avg:
    print('Gunnar')
else:
    print('Emma')