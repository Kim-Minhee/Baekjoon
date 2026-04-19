import sys
input = sys.stdin.readline

N = input().split()
for i, name in enumerate(N):
    if name == 'bubble' or name == 'tapioka':
        N[i] = ''
r = ' '.join(N).strip()
if r == '':
    print('nothing')
else:
    print(r)