import sys
input = sys.stdin.readline

while True:
    M = int(input())
    if M == 0:
        break
    
    a = M * M - M + 1
    s = M * (a + M - 1)
    if s == M ** 3:
        print('Y', a)
    else:
        print('N', 0)