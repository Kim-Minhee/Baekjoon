from collections import Counter
import sys
input = sys.stdin.readline

TEXT = input().strip().upper()
letter_counter = Counter(TEXT)
for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    print(f'{letter} |', end='')
    if letter in letter_counter:
        print(' ' + '*' * letter_counter[letter])
    else:
        print()