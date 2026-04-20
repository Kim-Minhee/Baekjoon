# GPT 5
import sys
input = sys.stdin.readline

N = int(input())

t_prev, d_prev = map(int, input().split())

max_speed = 0

for _ in range(N - 1):
    t, d = map(int, input().split())
    
    speed = (d - d_prev) // (t - t_prev)
    max_speed = max(max_speed, speed)
    
    t_prev, d_prev = t, d

print(max_speed)