import sys
input = sys.stdin.readline

def solve():
    N = list(map(int, input().split()))
    not_zero_num = []
    not_zero_idx = []
    for i, n in enumerate(N):
        if n != 0:
            not_zero_num.append(n)
            not_zero_idx.append(i)
    d = (not_zero_num[1] - not_zero_num[0]) / (not_zero_idx[1] - not_zero_idx[0])
    if not d.is_integer():
        print(-1)
        return
    else:
        d = int(d)
    
    if not_zero_idx[0] != 0:
        N[0] = not_zero_num[0] - (not_zero_idx[0] * d)
    for i in range(1, 10):
        N[i] = N[i - 1] + d
    print(*N)

if __name__ == '__main__':
    solve()