import sys
input = sys.stdin.readline

def chk_right_tri(t):
    if t[0] ** 2 + t[1] ** 2 == t[2] ** 2:
        return True
    return False

T1 = list(map(int, input().split()))
T2 = list(map(int, input().split()))
T1.sort()
T2.sort()
if T1 == T2 and chk_right_tri(T1):
    print('YES')
else:
    print('NO')