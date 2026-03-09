import sys
input = sys.stdin.readline

dies = {'::::o::::':1,
        'o:::::::o':2,
        '::o:::o::':2,
        '::o:o:o::':3,
        'o:::o:::o':3,
        'o:o:::o:o':4,
        'o:o:o:o:o':5,
        'ooo:::ooo':6,
        'o:oo:oo:o':6}

D = ''
for _ in range(3):
    D += input().strip()
if D in dies:
    print(dies[D])
else:
    print('unknown')