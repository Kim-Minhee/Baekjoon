# GPT 5
import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    s = input().strip()
    
    result = []
    cur = s[0]
    cnt = 1
    
    for c in s[1:]:
        if c == cur:
            cnt += 1
        else:
            result.append(f"{cnt} {cur}")
            cur = c
            cnt = 1
    
    # 마지막 블록 처리
    result.append(f"{cnt} {cur}")
    
    print(' '.join(result))