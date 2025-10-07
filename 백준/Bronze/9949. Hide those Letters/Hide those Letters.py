import sys
input = sys.stdin.readline

i = 1
while True:
    A, B = input().split()
    if A == B == '#':
        break
    sentences = [input().strip() for _ in range(int(input().strip()))]
    if i > 1:
        print()
    print(f'Case {i}')
    for sentence in sentences:
        print(sentence.replace(A, '_').replace(B, '_').replace(A.upper(), '_').replace(B.upper(), '_'))
    i += 1