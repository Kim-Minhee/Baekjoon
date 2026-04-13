# GPT 5
import sys
input = sys.stdin.readline

L, x = map(int, input().split())

cur = 0      # 현재 인원
denied = 0   # 거절된 횟수

for _ in range(x):
    cmd, p = input().split()
    p = int(p)
    
    if cmd == "enter":
        if cur + p > L:
            denied += 1
        else:
            cur += p
    else:  # leave
        cur -= p

print(denied)