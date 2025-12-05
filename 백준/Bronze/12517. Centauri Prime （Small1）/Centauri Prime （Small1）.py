import sys
input = sys.stdin.readline

for t in range(1, int(input().strip()) + 1):
    NAME = input().rstrip()
    answer = str()
    if NAME[-1] == 'y':
        answer = 'nobody'
    elif NAME[-1] in 'aeiou':
        answer = 'a queen'
    else:
        answer = 'a king'
    print(f'Case #{t}: {NAME} is ruled by {answer}.')