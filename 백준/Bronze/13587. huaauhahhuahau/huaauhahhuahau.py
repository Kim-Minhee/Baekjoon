import sys
input = sys.stdin.readline

L = input()
vowel = ''
for l in L:
    if l in 'aeiou':
        vowel += l
if vowel == vowel[::-1]:
    print('S')
else:
    print('N')