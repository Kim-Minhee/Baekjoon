S1, S2 = list(''.join(input().split())), list(''.join(input().split()))

S1.sort()
S2.sort()

print('Is an anagram.' if S1==S2 else 'Is not an anagram.')