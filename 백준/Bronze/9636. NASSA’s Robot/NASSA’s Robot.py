# GPT 5
import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    s = input().strip()
    u = s.count('U')
    d = s.count('D')
    l = s.count('L')
    r = s.count('R')
    q = s.count('?')

    x = r - l
    y = u - d

    min_x = x - q
    max_x = x + q
    min_y = y - q
    max_y = y + q

    print(min_x, min_y, max_x, max_y)