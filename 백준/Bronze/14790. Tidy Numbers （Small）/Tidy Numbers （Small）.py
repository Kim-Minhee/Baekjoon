# GPT 5.1
import sys
input = sys.stdin.readline

def is_tidy(x):
    s = str(x)
    return all(s[i] <= s[i+1] for i in range(len(s)-1))

T = int(input().strip())

for t in range(1, T + 1):
    N = int(input().strip())
    
    # N부터 내려오면서 마지막 tidy 숫자 찾기
    answer = 1
    for x in range(N, 0, -1):
        if is_tidy(x):
            answer = x
            break
    
    print(f"Case #{t}: {answer}")