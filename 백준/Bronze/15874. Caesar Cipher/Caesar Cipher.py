import sys
input = sys.stdin.readline

k, length = map(int, input().split())
s = input().rstrip('\n')

k %= 26

result = []

for c in s:
    if 'A' <= c <= 'Z':
        new_c = chr((ord(c) - ord('A') + k) % 26 + ord('A'))
        result.append(new_c)
    elif 'a' <= c <= 'z':
        new_c = chr((ord(c) - ord('a') + k) % 26 + ord('a'))
        result.append(new_c)
    else:
        result.append(c)

print(''.join(result))