import sys
input = sys.stdin.readline

def chk_happy(num):
    str_num = str(num)
    r = 0
    for n in str_num:
        r += int(n) ** 2
    return r

N = int(input().strip())
while True:
    if N == 1:
        print('HAPPY')
        break
    elif N in [4, 16, 37, 58, 89, 145, 42, 20]:
        print('UNHAPPY')
        break
    N = chk_happy(N)