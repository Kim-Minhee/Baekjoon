# GPT 4o
T = int(input())
for _ in range(T):
    s = input().strip()
    # 모든 회전 중 사전순 최소 선택
    min_rotation = min(s[i:] + s[:i] for i in range(len(s)))
    print(min_rotation)