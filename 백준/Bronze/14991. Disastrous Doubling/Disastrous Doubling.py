import sys
input = sys.stdin.readline

N = int(input().strip())
B = list(map(int, input().split()))
cur_b = 1
error_chk = False
for hour in range(1, N + 1):
    cur_b *= 2
    need_b = B[hour - 1]
    if cur_b < need_b:
        print('error')
        error_chk = True
        break
    cur_b -= need_b
if not error_chk:
    print(cur_b % 1000000007)