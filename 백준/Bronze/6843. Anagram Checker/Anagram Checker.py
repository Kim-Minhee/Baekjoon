# GPT 4o
from collections import Counter

S1 = Counter(input().replace(' ', ''))
S2 = Counter(input().replace(' ', ''))

if S1 == S2:
    print('Is an anagram.')
else:
    print('Is not an anagram.')