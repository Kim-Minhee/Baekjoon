# GPT 5
import sys
input = sys.stdin.readline

msg = input().strip()
crib = input().strip()

n = len(msg)
m = len(crib)

count = 0

for start in range(n - m + 1):
    ok = True
    for i in range(m):
        if msg[start + i] == crib[i]:
            ok = False
            break
    if ok:
        count += 1

print(count)