# GPT 5
import sys
input = sys.stdin.readline

N = int(input())
total = 0

for _ in range(N):
    x, y = map(int, input().split())
    
    d2 = x*x + y*y  # sqrt 안 쓰고 제곱으로 비교
    
    if d2 <= 10*10:
        total += 10
    elif d2 <= 30*30:
        total += 9
    elif d2 <= 50*50:
        total += 8
    elif d2 <= 70*70:
        total += 7
    elif d2 <= 90*90:
        total += 6
    elif d2 <= 110*110:
        total += 5
    elif d2 <= 130*130:
        total += 4
    elif d2 <= 150*150:
        total += 3
    elif d2 <= 170*170:
        total += 2
    elif d2 <= 190*190:
        total += 1
    else:
        total += 0

print(total)