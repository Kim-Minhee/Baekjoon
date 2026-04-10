import sys
input = sys.stdin.readline

r = 'Anywhere is fine I guess'
for _ in range(int(input().strip())):
    K = int(input().strip())
    R = input().strip()
    menus = set(input().strip() for _ in range(K))
    if 'pea soup' in menus and 'pancakes' in menus and r == 'Anywhere is fine I guess':
        r = R
print(r)