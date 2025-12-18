# GPT 5.2
import sys
input = sys.stdin.readline

s = input().strip()

vowels = 'aeiou'
only_vowels = ''.join(c for c in s if c in vowels)

if only_vowels == only_vowels[::-1]:
    print('S')
else:
    print('N')