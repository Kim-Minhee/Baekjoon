import sys
input = sys.stdin.readline

def div_chk(num):
    str_num = str(num)
    for n in str_num:
        if num % int(n) != 0:
            return False
    return True

L, H = map(int, input().split())
c = 0
for num in range(L, H + 1):
    str_num = str(num)
    if '0' in str_num:
        continue
    if len(set(str_num)) != 6:
        continue
    if div_chk(num):
        c += 1
print(c)