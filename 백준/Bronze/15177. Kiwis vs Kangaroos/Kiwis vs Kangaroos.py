import sys
input = sys.stdin.readline

kang = {'k':1, 'a':2, 'n':1, 'g':1, 'r':1, 'o':2}
kiwi = {'k':1, 'i':3, 'w':1, 'b':1, 'r':1, 'd':1}

S = input().strip().lower()
score_kang, score_kiwi = 0, 0
for s in S:
    if s in kang:
        score_kang += kang[s]
    if s in kiwi:
        score_kiwi += kiwi[s]
if score_kang > score_kiwi:
    print('Kangaroos')
elif score_kang < score_kiwi:
    print('Kiwis')
else:
    print('Feud continues')