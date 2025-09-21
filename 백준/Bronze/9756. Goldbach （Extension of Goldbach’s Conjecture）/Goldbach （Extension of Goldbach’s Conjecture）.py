# GPT 5
import sys
input = sys.stdin.readline

while True:
    m = int(input().strip())
    if m == 0:
        break
    # 항상 가능
    first_odd = m * m - m + 1
    print("Y", first_odd)