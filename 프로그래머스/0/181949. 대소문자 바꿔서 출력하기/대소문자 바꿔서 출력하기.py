str = input()
r = []
for s in str:
    if 'A' <= s <= 'Z':
        r.append(s.lower())
    else:
        r.append(s.upper())
print(''.join(r))