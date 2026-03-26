# GPT 5
import sys
input = sys.stdin.readline

pt, p1, p2 = map(float, input().split())

# 센트 단위로 변환
pt = int(round(pt * 100))
p1 = int(round(p1 * 100))
p2 = int(round(p2 * 100))

found = False

# 피타 개수 x 기준 (작은 순서 출력)
for x in range(pt // p1 + 1):
    remain = pt - x * p1
    
    if remain < 0:
        break
    
    # 피자 개수 y 계산 가능 여부
    if remain % p2 == 0:
        y = remain // p2
        print(x, y)
        found = True

if not found:
    print("none")