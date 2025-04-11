# GPT
import sys

S = input()

for L in sys.stdin:
    L = L.strip()
    temp_s = ''
    for i, l in enumerate(L):
        s = (int(S[i]) + int(l)) % 10
        temp_s += str(s)
    S = temp_s

print(S)