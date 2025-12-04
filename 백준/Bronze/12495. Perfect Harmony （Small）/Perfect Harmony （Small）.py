import sys, math
input = sys.stdin.readline

def harmony_chk(a, b):
    if a % b == 0 or b % a == 0:
        return True
    return False

for t in range(1, int(input().strip()) + 1):
    N, L, H = map(int, input().split())
    F = list(map(int, input().split()))
    if L == 1:
        print(f'Case #{t}: 1')
        continue
    end_chk = False
    for jeff in range(L, H + 1):
        find_chk = True
        for freq in F:
            if not harmony_chk(jeff, freq):
                find_chk = False
                break
        if find_chk:
            print(f'Case #{t}: {jeff}')
            end_chk = True
            break
    if not end_chk:
        print(f'Case #{t}: NO')