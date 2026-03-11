# GPT 5
import sys
input = sys.stdin.readline

L, H = map(int, input().split())

cnt = 0

for c in range(L, H + 1):
    s = str(c)
    
    # 0 포함 여부
    if '0' in s:
        continue
    
    # 서로 다른 숫자
    if len(set(s)) != 6:
        continue
    
    # 각 자리 숫자로 나누어 떨어지는지
    ok = True
    for d in s:
        if c % int(d) != 0:
            ok = False
            break
    
    if ok:
        cnt += 1

print(cnt)