# GPT 5
import sys
input = sys.stdin.readline

T = int(input().strip())
for t in range(1, T + 1):
    n, P, Q = map(int, input().split())
    eggs = list(map(int, input().split()))
    eggs.sort()

    total_weight = 0
    count = 0
    for w in eggs:
        if count + 1 > P:  # 개수 제한
            break
        if total_weight + w > Q:  # 무게 제한
            break
        count += 1
        total_weight += w

    print(f"Case {t}: {count}")