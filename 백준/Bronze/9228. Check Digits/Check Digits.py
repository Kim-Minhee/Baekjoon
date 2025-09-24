import sys
input = sys.stdin.readline

while True:
    NUM = list(input().strip())
    if NUM[0] == '#':
        break
    total, i = 0, 2
    for n in NUM[::-1]:
        total += int(n) * i
        i += 1
    chk_num = 11 - total % 11
    if chk_num == 11:
        chk_num = 0
    elif chk_num == 10:
        chk_num = 'Rejected'
    print(f"{''.join(NUM)} -> {chk_num}")