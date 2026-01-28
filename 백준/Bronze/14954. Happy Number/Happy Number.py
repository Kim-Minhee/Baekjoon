# GPT 5.1
import sys
input = sys.stdin.readline

def f(n):
    return sum((int(c) ** 2) for c in str(n))

n = int(input().strip())
visited = set()

while n != 1 and n not in visited:
    visited.add(n)
    n = f(n)

if n == 1:
    print("HAPPY")
else:
    print("UNHAPPY")