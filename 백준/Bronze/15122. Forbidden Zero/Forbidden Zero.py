# GPT 5.1
import sys
input = sys.stdin.readline

n = int(input().strip())
x = n + 1

while '0' in str(x):
    x += 1

print(x)