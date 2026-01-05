import sys
input = sys.stdin.readline

for t in range(1, int(input().strip()) + 1):
    max_ch_cnt = 0
    name = ''
    for n in range(int(input().strip())):
        NAME = input().rstrip()
        ch_list = set()
        for ch in NAME:
            if 'A' <= ch <= 'Z':
                ch_list.add(ch)
        ch_cnt = len(ch_list)
        if max_ch_cnt < ch_cnt or (max_ch_cnt == ch_cnt and NAME < name):
            max_ch_cnt = ch_cnt
            name = NAME
    print(f'Case #{t}: {name}')