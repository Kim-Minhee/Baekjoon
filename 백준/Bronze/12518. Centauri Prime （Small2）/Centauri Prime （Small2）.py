import sys
input = sys.stdin.readline

for t in range(1, int(input().strip()) + 1):
    NAME = input().rstrip()
    last_chr = NAME[-1].lower()
    if last_chr == 'y':
        answer = 'nobody'
    elif last_chr in 'aeiou':
        answer = 'a queen'
    else:
        answer = 'a king'
    print(f'Case #{t}: {NAME} is ruled by {answer}.')