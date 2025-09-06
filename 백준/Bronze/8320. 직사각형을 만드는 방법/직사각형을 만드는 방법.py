# GPT 5
import sys

n = int(sys.stdin.readline())
ans = 0
a = 1
while a * a <= n:
    # b는 a 이상이면서 a*b <= n인 정수의 개수
    ans += n // a - (a - 1)
    a += 1
print(ans)