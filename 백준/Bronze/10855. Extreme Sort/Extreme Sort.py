# GPT 5
import sys
input = sys.stdin.readline

N = int(input().strip())
a = list(map(int, input().split()))

# 비내림 순서인지 확인
ok = all(a[i] <= a[i+1] for i in range(N-1))

print("yes" if ok else "no")