# GPT 5
import sys
input = sys.stdin.readline

words = input().split()

res = []
for w in words:
    if w != "bubble" and w != "tapioka":
        res.append(w)

if not res:
    print("nothing")
else:
    print(' '.join(res))