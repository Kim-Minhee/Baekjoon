import sys
input = sys.stdin.readline

keyboard = {'a':2, 'b':2, 'c':2,
            'd':3, 'e':3, 'f':3,
            'g':4, 'h':4, 'i':4,
            'j':5, 'k':5, 'l':5,
            'm':6, 'n':6, 'o':6,
            'p':7, 'q':7, 'r':7, 's':7,
            't':8, 'u':8, 'v':8,
            'w':9, 'x':9, 'y':9, 'z':9}
word_to_num = {}
for _ in range(int(input().strip())):
    W = input().strip()
    num = [str(keyboard[w]) for w in W]
    str_num = ''.join(num)
    word_to_num[str_num] = word_to_num.get(str_num, 0) + 1
S = input().strip()
print(word_to_num.get(S, 0))