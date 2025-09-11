import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = input().strip()
    try:
        n = int(N)
        if n >= 0:
            print(n)
        else:
            print('invalid input')
    except:
        print('invalid input')