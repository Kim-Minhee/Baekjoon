import sys
input = sys.stdin.readline

def last_num(num):
    if len(num) >= 4:
        return num[-4:]
    return num.zfill(4)

def find_group(num):
    if num == '00':
        num = '100'
    return (int(num) - 1) // 4

while True:
    DATA = input().split()
    if DATA == ['0', '0', '0']:
        break
    
    v, n, m = float(DATA[0]), last_num(DATA[1]), last_num(DATA[2])
    r = 0
    if n == m:
        r = v * 3000
    elif n[1:] == m[1:]:
        r = v * 500
    elif n[2:] == m[2:]:
        r = v * 50
    elif find_group(n[2:]) == find_group(m[2:]):
        r = v * 16
    print(f'{r:.2f}')