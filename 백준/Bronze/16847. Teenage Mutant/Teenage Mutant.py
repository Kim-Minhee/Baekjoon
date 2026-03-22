# GPT 5
import sys
input = sys.stdin.readline

K = int(input())

for tc in range(1, K + 1):
    n, k = map(int, input().split())
    
    me = input().strip()
    ancestors = [input().strip() for _ in range(n)]
    
    mutant = 0
    
    for i in range(k):
        is_mutant = True
        for j in range(n):
            if ancestors[j][i] == me[i]:
                is_mutant = False
                break
        if is_mutant:
            mutant += 1
    
    print(f"Data Set {tc}:")
    print(f"{mutant}/{k}")
    print()