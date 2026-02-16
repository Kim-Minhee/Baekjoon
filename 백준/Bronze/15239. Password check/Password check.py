import sys, re
input = sys.stdin.readline

def chk_valid(password):
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[+_)(*&^%$#@!./,;{}]', password):
        return False
    return True

N = int(input().strip())
for _ in range(N):
    S = int(input().strip())
    P = input().strip()
    if S < 12:
        print('invalid')
        continue
    if chk_valid(P):
        print('valid')
    else:
        print('invalid')