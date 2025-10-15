import sys
input = sys.stdin.readline

ch = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'

while True:
    DATA = input().split()
    if DATA[0] == '0':
        break
    n, sentence = int(DATA[0]), DATA[1][::-1]
    r = []
    for s in sentence:
        r.append(ch[(ch.index(s) + n) % 28])
    print(''.join(r))