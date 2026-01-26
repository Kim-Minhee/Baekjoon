# GPT 5.1
import sys
input = sys.stdin.readline

K = int(input().strip())

for case in range(1, K + 1):
    n, v = map(int, input().split())
    
    # 광고 정보 저장
    # ads[i] = (di, pi)
    ads = [None]  # 1-based index 사용
    for _ in range(n):
        di, pi = map(int, input().split())
        ads.append((di, pi))
    
    total = 0
    
    # 방문자 정보 처리
    for _ in range(v):
        a1, a2, c = map(int, input().split())
        
        # 디스플레이 광고면 보기만 해도 돈을 받음
        d1, p1 = ads[a1]
        d2, p2 = ads[a2]
        
        if d1 == 1:
            total += p1
        if d2 == 1:
            total += p2
        
        # 클릭 유도 광고라면 클릭했을 때만 돈을 받음
        if c == 1:   # a1 클릭
            if d1 == 0:
                total += p1
        elif c == 2: # a2 클릭
            if d2 == 0:
                total += p2
    
    print(f"Data Set {case}:")
    print(total)
    print()