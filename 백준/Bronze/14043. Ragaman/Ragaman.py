from collections import Counter
import sys
input = sys.stdin.readline

A = input().strip()
B = input().strip()
a_counter = Counter(A)
b_counter = Counter(B)
ana_chk = True
for key, value in b_counter.items():
    if key == '*':
        continue
    if key not in a_counter or a_counter[key] - value < 0:
        ana_chk = False
        break
    a_counter[key] -= value

if b_counter['*'] != sum(a_counter.values()):
    ana_chk = False

if ana_chk:
    print('A')
else:
    print('N')