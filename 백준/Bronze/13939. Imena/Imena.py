import sys
input = sys.stdin.readline

def is_name(word):
    if not ('A' <= word[0] <= 'Z'):
        return False
    for w in word[1:]:
        if not ('a' <= w <= 'z') or w in '0123456789':
            return False
    return True

N = int(input().strip())
S = input().strip()
S = S.replace('.', '\n')
S = S.replace('?', '\n')
S = S.replace('!', '\n')
S = S.split('\n')

for sentence in S:
    if sentence == '':
        continue
    name_cnt = 0
    for word in sentence.split():
        if is_name(word):
            name_cnt += 1
    print(name_cnt)