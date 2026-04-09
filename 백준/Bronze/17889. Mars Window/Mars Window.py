# GPT 5
import sys
input = sys.stdin.readline

y = int(input().strip())

# 시작 시점 (월 단위)
start = 2018 * 12 + 4

# 해당 연도의 시작/끝
year_start = y * 12 + 1
year_end = y * 12 + 12

cur = start

while cur <= year_end:
    if year_start <= cur <= year_end:
        print("yes")
        break
    cur += 26
else:
    print("no")