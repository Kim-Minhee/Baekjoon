import sys
input = sys.stdin.readline

right, wrong = {}, {}
total_pnt = 0

while True:
    L = input().strip()
    if L == '-1':
        break
    m, p, r = L.split()
    if r == 'right':
        right[p] = int(m)
    elif p not in right.keys():
        wrong[p] = wrong.get(p, 0) + 1

for problem, minutes in right.items():
    pnt = minutes
    if problem in wrong.keys():
        pnt += wrong[problem] * 20
    total_pnt += pnt

print(len(right), total_pnt)