import sys
input = sys.stdin.readline

def reverse(s):
    return s[::-1]

def switch(s):
    new_s = []
    for n in s:
        if n == '0':
            new_s.append('1')
        else:
            new_s.append('0')
    return ''.join(new_s)

for t in range(1, int(input().strip()) + 1):
    K = int(input().strip())
    s = ''
    while True:
        reverse_s = reverse(s)
        switch_s = switch(reverse_s)
        s = s + '0' + switch_s
        if len(s) >= K:
            print(f'Case #{t}: {s[K - 1]}')
            break