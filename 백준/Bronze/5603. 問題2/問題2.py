# GPT
from itertools import groupby

def change_string(s):
    return ''.join(f"{len(list(g))}{k}" for k, g in groupby(s))

n = int(input())
s = input()
for _ in range(n):
    s = change_string(s)

print(s)