# GPT 5
import sys
input = sys.stdin.readline

T = int(input().strip())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    D = list(map(int, input().split()))

    from collections import Counter
    
    # (a ^ b) 값들의 등장 횟수 계산
    ab_counts = Counter()
    for a in A:
        for b in B:
            ab_counts[a ^ b] += 1
    
    answer = 0
    # (c ^ d)를 구하며 필요한 (a^b) 존재 여부 확인
    for c in C:
        for d in D:
            need = (c ^ d) ^ K
            if need in ab_counts:
                answer += ab_counts[need]

    print(f"Case #{tc}: {answer}")