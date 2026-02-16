# GPT 5.1
import sys
input = sys.stdin.readline

symbols = set("+_)(*&^%$#@!./,;{}")

T = int(input().strip())

for _ in range(T):
    S = int(input().strip())
    pw = input().strip()
    
    if (
        S >= 12 and
        any(c.islower() for c in pw) and
        any(c.isupper() for c in pw) and
        any(c.isdigit() for c in pw) and
        any(c in symbols for c in pw)
    ):
        print("valid")
    else:
        print("invalid")